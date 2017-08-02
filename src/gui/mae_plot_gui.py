'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTreeWidgetItem
from matplotlibwidget import MatplotlibWidget
from inout.streamcimh5 import StreamCIMH5
# from matplotlib.backends.backend_qt4agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
# import matplotlib.pyplot as plt

form_gui = uic.loadUiType("./res/mae_plot_gui.ui")[0] # Load the UI

class UI_Plot_MAE(QtGui.QDialog, form_gui):
    
    __measurements= None
    __dbh5api= None
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.load_h5db()
        #
        self.mplotwidget = MatplotlibWidget(self.centralWidget)
        self.mplotwidget.setGeometry(QtCore.QRect(0, 0, 520, 380))
        self.mplotwidget.setObjectName("mplotwidget")
        #
        self.twVariable.itemSelectionChanged.connect(self.__onSelectionChanged)
        #
        self.cbxMeasurements.activated['QString'].connect(self.__loadSignals)
        #
        self.btnLoadSignals.clicked.connect(self.__loadSignals)
            
    def load_h5db(self):
        fsm = QtGui.QFileSystemModel()
        index = fsm.setRootPath("./db/h5")
        self.cbxMeasurements.setModel(fsm)
        self.cbxMeasurements.setRootModelIndex(index)
    
    def __loadSignals(self, text):
        ''' load signals from the h5 database '''
        self.__measurements= str(text) #h5 file name 
        self.__dbh5api= StreamCIMH5('./db/h5', self.__measurements)
        self.__dbh5api.open(self.__measurements, mode= 'r')
        # TODO select model, root group h5
        self.twVariable.clear()
        rootItem= QTreeWidgetItem(self.twVariable, [self.__dbh5api.select_Model()])
        # TODO select power system resource
        arbolMedidas= self.__dbh5api.select_AllGroup(self.__dbh5api.select_Model())
        for psres in arbolMedidas:
            print "%s: %s" % (psres, arbolMedidas[psres]) 
            itemParent= QTreeWidgetItem()
            itemParent.setText(0,unicode(psres))
            for psmeas in arbolMedidas[psres]:
                childItem = QTreeWidgetItem()
                childItem.setText(0, unicode(psmeas))
                itemParent.addChild(childItem)
            rootItem.addChild(itemParent)
            
    def __onSelectionChanged(self):
        '''
        Update the variable's attributes and plot
        '''
        getSelected = self.twVariable.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            parentName= str(baseNode.parent().text(0))
            childName= baseNode.text(0)
            paramName= parentName+ '.'+ childName
        self.__view_Measurement(str(paramName))
        
    def __view_Measurement(self, name):
        '''Show the variable's attributes and a small plot. fix it using the matplotlibwidget
        Using H5 database for ploting measurement signals'''
        splitName= name.split('.')
        print '%s.%s' % (splitName[-2], splitName[-1])
        if self.__dbh5api.exist_PowerSystemResource(splitName[-2]):
            self.__dbh5api.select_PowerSystemResource(splitName[-2])
            senyal= self.__dbh5api.select_AnalogMeasurement(splitName[-1])
#             text = 'Name: ' + senyal['unitSymbol']
#             text += '\n' + 'Description: ' + senyal['unitMultiplier']
#             text += '\n' + 'unit: ' + senyal['measurementType']
#             text += '\n' + 'displayUnit: ' + senyal['measurementType']
            ''' TODO updated title, xAxis and yAxis labels
            TODO handle multiple signals- hold option
            TODO plot GUI to accept HDF5 format
            TODO export to CSV '''
            self.mplotwidget.theplot.set_title('Something here')
            self.mplotwidget.theplot.set_xlabel('Time (s)')
            self.mplotwidget.theplot.set_ylabel('Magnitude (unit)')
            self.mplotwidget.plot(senyal['sampleTime'], senyal['magnitude'])
        else:
            print "nothing to plot"
        # TODO select analog measurement and analogvalue
        # TODO use pycim to store psres and am and av
        
        
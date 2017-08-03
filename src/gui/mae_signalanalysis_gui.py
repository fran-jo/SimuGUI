'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTableWidget, QTreeWidgetItem
from modelicares import util, SimRes
from matplotlibwidget import MatplotlibWidget
from inout.streamcimh5 import StreamCIMH5
# from matplotlib.backends.backend_qt4agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
# import matplotlib.pyplot as plt

__form_gui = uic.loadUiType("./res/mae_signalanalysis_gui.ui")[0] # Load the UI

class UI_SignalAnalysis(QtGui.QDialog, __form_gui):
    
    __simResults= None
    __measurements= None
    
    def __init__(self, parent= None, simulationResults= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.mplotwidget = MatplotlibWidget(self.mplotWidget)
        self.mplotwidget.setGeometry(QtCore.QRect(0, 0, 470, 312))
        self.mplotwidget.setObjectName("mplotSimwidget")
        #
        self.cbxOutputs.activated['QString'].connect(self.__load_OutputSignals)
        self.onLoad_populateOutputFiles()
        #
        self.cbxMeasurements.activated['QString'].connect(self.__load_Measurements)
        self.onLoad_populateMeasurements()
        
    def onLoad_populateOutputFiles(self):
        ''' list in the combobox all the outputs files from Dy, OMC, JM '''
        ''' files from DY '''
        path= QtCore.QDir('./res/dy')
        files= path.entryList(QtCore.QDir.Files, QtCore.QDir.Name)
        self.cbxOutputs.addItems(['./res/dy/'+ f for f in files])
        ''' files from OMC '''
        path= QtCore.QDir('./res/omc')
        files= path.entryList(QtCore.QDir.Files, QtCore.QDir.Name)
        self.cbxOutputs.addItems(['./res/omc/'+ f for f in files])
        
    def onLoad_populateMeasurements(self):
        ''' list in the combobox all the outputs files from H5'''
        path= QtCore.QDir('./db/h5')
        files= path.entryList(QtCore.QDir.Files, QtCore.QDir.Name)
        self.cbxMeasurements.addItems(files)
        
    # This function has been copied and modified from ModelicaRes version 0.12
    # (Kevin Davies,
    # http://kdavies4.github.io/ModelicaRes/,
    # BSD License)
    def __load_OutputSignals(self, outputmatfile):
        '''
        open mat file and populate variables  
        '''
        self.__results= SimRes(str(outputmatfile))
        arbol = util.tree(self.__results.names())
        self.twOutVariable.clear()
        rootItem= QTreeWidgetItem(self.twOutVariable, [self.__results.fbase])
        self.__build_tree(rootItem, arbol)
        self.twOutVariable.itemSelectionChanged.connect(self.__twOutVariable_onSelectionChanged)
    
    # This function has been copied and modified from ModelicaRes version 0.12
    # (Kevin Davies,
    # http://kdavies4.github.io/ModelicaRes/,
    # BSD License).
    def __build_tree(self, itemParent=None, branches=None):
        #itemParent.setExpanded(True)
        if type(branches) is dict:
            for key, val in sorted(branches.iteritems()):
                childItem = QTreeWidgetItem()
                childItem.setText(0, unicode(key))
                itemParent.addChild(childItem)
                if type(val) is dict:
                    self.__build_tree(childItem, val)
        else:
            childItem = QTreeWidgetItem()
            childItem.setText(0, unicode(branches))
            itemParent.addChild(childItem)
    
    def __twOutVariable_onSelectionChanged(self):
        """Update the variable's attributes and plot.
        """
        getSelected = self.twOutVariable.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            parentName= str(baseNode.parent().text(0))
            childName= baseNode.text(0)
            if baseNode.parent().parent()!= None:
                grandpaName= str(baseNode.parent().parent().text(0))
            if grandpaName== self.__results.fbase:
                paramName= parentName+ '.'+ childName
            else:
                paramName= grandpaName+ '.'+ parentName+ '.'+ childName
        self.__view_Signal(str(paramName), self.__results)
    
    # This function has been copied and modified from ModelicaRes version 0.12
    # (Kevin Davies,
    # http://kdavies4.github.io/ModelicaRes/,
    # BSD License)
    def __view_Signal(self, name, sim):
        '''Show the variable's attributes and a small plot.
        fix it using the matplotlibwidget
        Using ModelicaRes for ploting simulation signals'''
        if name:
            text = 'Name: ' + name
            text += '\n' + 'Description: ' + sim[name].description
            text += '\n' + 'unit: ' + sim[name].unit
            text += '\n' + 'displayUnit: ' + sim[name].displayUnit
            self.mplotwidget.theplot.set_title('Something here')
            self.mplotwidget.theplot.set_xlabel('Time (s)')
            self.mplotwidget.theplot.set_ylabel(sim[name].description)
            self.mplotwidget.plot(sim[name].times().tolist(), sim[name].values().tolist())
        else:
            print "nothing to plot"

    def __load_Measurements(self, dbh5file):
        ''' load signals from the h5 database '''
        self.__measurements= str(dbh5file) #h5 file name 
        self.__dbh5api= StreamCIMH5('./db/h5', self.__measurements)
        self.__dbh5api.open(self.__measurements, mode= 'r')
        # TODO select model, root group h5
        self.twMeasVariable.clear()
        rootItem= QTreeWidgetItem(self.twMeasVariable, [self.__dbh5api.select_Model()])
        arbolMedidas= self.__dbh5api.select_AllGroup(self.__dbh5api.select_Model())
        for psres in arbolMedidas:
            itemParent= QTreeWidgetItem()
            itemParent.setText(0,unicode(psres))
            for psmeas in arbolMedidas[psres]:
                childItem = QTreeWidgetItem()
                childItem.setText(0, unicode(psmeas))
                itemParent.addChild(childItem)
            rootItem.addChild(itemParent)
        self.twMeasVariable.itemSelectionChanged.connect(self.__twMeasVariable_onSelectionChanged)
        
    def __twMeasVariable_onSelectionChanged(self):
        '''
        Update the variable's attributes and plot
        '''
        getSelected = self.twMeasVariable.selectedItems()
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
    
    def __saveAnalysis(self):
        pass
    
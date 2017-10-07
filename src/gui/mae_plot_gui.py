'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTreeWidgetItem
from inout.streamh5cim import StreamH5CIM
from mae_importdata_gui import UI_ImportData
from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

'''TODO Import Selected variables into H5 '''
'''TODO handel multiple selection '''

form_gui = uic.loadUiType("./res/mae_plot_gui.ui")[0] # Load the UI

class UI_Plot_MAE(QtGui.QDialog, form_gui):
    
    __measurements= None
    __dbh5api= None
    
    def __init__(self, parent):
        super(UI_Plot_MAE, self).__init__(parent)
        self.setupUi(self)
        self.load_h5db()
        #
#         self.mplotwidget = MatplotlibWidget(self.centralWidget, width= 590, height= 380, dpi= 60)
#         self.mplotwidget.setGeometry(QtCore.QRect(0, 0, 590, 380))
#         self.mplotwidget.setObjectName("mplotwidget")
        self.createGraficaMeas()
        #
        self.twVariable.itemSelectionChanged.connect(self.__onSelectionChanged)
        #
        self.cbxMeasurements.activated['QString'].connect(self.__loadSignals)
        #
        self.btnLoadSignals.clicked.connect(self.__loadSignals)
        #
        self.btnImportMeasurements.clicked.connect(self.__openImportDialog)

    def createGraficaMeas(self):
        self.figureGM = plt.figure(figsize=(590, 380), dpi=80)
        self.canvasGM = FigureCanvas(self.figureGM)
        self.toolbarGM = NavigationToolbar(self.canvasGM, self)
        self.graficaGM = self.figureGM.add_subplot(111) 
        self.graficaGM.grid()
        # set the layout
        layoutGM = QtGui.QVBoxLayout()
        layoutGM.addWidget(self.canvasGM)
        layoutGM.addWidget(self.toolbarGM)
        layoutGM.setContentsMargins(0,0,0,0)
        self.centralWidget.setLayout(layoutGM)
        
            
    def load_h5db(self):
        fsm = QtGui.QFileSystemModel()
        index = fsm.setRootPath("./db/measurements")
        self.cbxMeasurements.setModel(fsm)
        self.cbxMeasurements.setRootModelIndex(index)
    
    def __loadSignals(self, text):
        ''' load signals from the h5 database '''
        self.__measurements= str(text) #h5 file name 
        self.__dbh5api= StreamH5CIM('./db/measurements', self.__measurements)
        self.__dbh5api.open(self.__measurements, mode= 'r')
        # TODO select model, root group h5
        self.twVariable.clear()
        rootItem= QTreeWidgetItem(self.twVariable, [self.__dbh5api.modelName])
        # TODO select power system resource
        arbolMedidas= self.__dbh5api.select_treeMeasurements(self.__dbh5api.modelName)
        for psres in arbolMedidas:
#             print "%s: %s" % (psres, arbolMedidas[psres]) 
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
        componentname= splitName[-3] if len(splitName)== 3 else splitName[-2]
        variablename= splitName[-2]+ '.'+ splitName[-1] if len(splitName)== 3 else splitName[-1]
        print '%s.%s' % (componentname, variablename)
        if self.__dbh5api.exist_PowerSystemResource(componentname):
            self.__dbh5api.select_PowerSystemResource(componentname)
            self.__dbh5api.select_AnalogMeasurement(variablename)
            self.graficaGM.clear()
            self.graficaGM.plot(self.__dbh5api.analogMeasurementValues['sampleTime'], 
                                self.__dbh5api.analogMeasurementValues['magnitude'])
            self.graficaGM.set_title("Signal", fontsize=12)
            self.graficaGM.set_xlabel("Time (s)", fontsize=10)
            self.graficaGM.set_ylabel("Magnitude (Unit)", fontsize=10)
            self.cursor = Cursor(self.graficaGM, lw = 2)
            self.graficaGM.grid()
            self.canvasGM.draw()
        else:
            print "nothing to plot"
        # TODO select analog measurement and analogvalue
        # TODO use pycim to store psres and am and av
    
    def __openImportDialog(self):
        importdialog = UI_ImportData(self)
        importdialog.setWindowTitle('Import Measurements to DB')
        importdialog.show() 
        
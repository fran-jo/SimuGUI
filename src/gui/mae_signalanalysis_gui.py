'''
Created on 19 jan 2016

@author: fragom
'''
'''TODO add a tab page for each source (simulation,measurement) '''
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTreeWidgetItem
from matplotlibwidget import MatplotlibWidget
from inout.streamh5cim import StreamH5CIM
from gui import UI_ModeEstimation

__form_gui = uic.loadUiType("./res/mae_signalanalysis_gui.ui")[0] # Load the UI

class UI_SignalAnalysis(QtGui.QDialog, __form_gui):
    
    __simulation= None
    __measurement= None
    __simudb= None
    __measdb= None
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.plotSimu = MatplotlibWidget(self.mplotSimulation, width= 440, height= 225, dpi= 60)
        self.plotSimu.setGeometry(QtCore.QRect(0, 0, 440, 225))
        self.plotSimu.setObjectName("mplotSimwidget")
        self.plotMeas = MatplotlibWidget(self.mplotMeasurements, width= 440, height= 225, dpi= 60)
        self.plotMeas.setGeometry(QtCore.QRect(0, 0, 440, 225))
        self.plotMeas.setObjectName("mplotMeaswidget")
        #
        self.cbxOutputs.activated['QString'].connect(self.__load_OutputSignals)
        self.onLoad_populateOutputFiles()
        #
        self.cbxMeasurements.activated['QString'].connect(self.__load_Measurements)
        self.onLoad_populateMeasurements()
        # menu items
        self.action_ModeEstimation.setShortcut('Ctrl+M')
        self.action_ModeEstimation.setStatusTip('Mode Estimation based on Signals')
        self.action_ModeEstimation.triggered.connect(self.show_meGUI)
        
    def onLoad_populateOutputFiles(self):
        ''' List in the combobox all the outputs files from the database of Dy, OMC, JM results 
        .h5 files
        '''
        path= QtCore.QDir('./db/simulation')
        files= path.entryList(QtCore.QDir.Files, QtCore.QDir.Name)
        self.cbxOutputs.addItems(files)
        
    def onLoad_populateMeasurements(self):
        ''' list in the combobox all the measurement files from the database
        .h5 files'''
        path= QtCore.QDir('./db/measurements')
        files= path.entryList(QtCore.QDir.Files, QtCore.QDir.Name)
        self.cbxMeasurements.addItems(files)
        
    def __load_OutputSignals(self, simulationh5):
        '''' load signals from the h5 database '''
        self.__simudb= StreamH5CIM('./db/simulation', str(simulationh5))
        self.__simudb.open(str(simulationh5), mode= 'r')
        # TODO select model, root group h5
        self.twOutVariable.clear()
        rootItem= QTreeWidgetItem(self.twOutVariable, [self.__simudb.modelName])
        arbolMedidas= self.__simudb.select_treeMeasurements(self.__simudb.modelName)
        for psres in arbolMedidas:
            itemParent= QTreeWidgetItem()
            itemParent.setText(0,unicode(psres))
            for psmeas in arbolMedidas[psres]:
                childItem = QTreeWidgetItem()
                childItem.setText(0, unicode(psmeas))
                itemParent.addChild(childItem)
            rootItem.addChild(itemParent)
        self.twOutVariable.itemSelectionChanged.connect(self.__twOutVariable_onSelectionChanged)
    
    def __twOutVariable_onSelectionChanged(self):
        '''
        Update the variable's attributes and plot
        '''
        getSelected = self.twOutVariable.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            parentName= str(baseNode.parent().text(0))
            childName= baseNode.text(0)
        if self.__simudb.exist_PowerSystemResource(str(parentName)):
            self.__simudb.select_PowerSystemResource(str(parentName))
            self.__simudb.select_AnalogMeasurement(str(childName))
            self.__simulation= self.__simudb.analogMeasurementValues
        self.__view_Measurement(self.plotSimu, self.__simulation, hold= False)

    def __load_Measurements(self, dbh5file):
        ''' load signals from the h5 database '''
        self.__measdb= StreamH5CIM('./db/measurements', str(dbh5file))
        self.__measdb.open(str(dbh5file), mode= 'r')
        # TODO select model, root group h5
        self.twMeasVariable.clear()
        rootItem= QTreeWidgetItem(self.twMeasVariable, [self.__measdb.modelName])
        arbolMedidas= self.__measdb.select_treeMeasurements(self.__measdb.modelName)
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
        if self.__measdb.exist_PowerSystemResource(str(parentName)):
            self.__measdb.select_PowerSystemResource(str(parentName))
            self.__measdb.select_AnalogMeasurement(str(childName))
            self.__measurement= self.__measdb.analogMeasurementValues
        self.__view_Measurement(self.plotMeas, self.__measurement, hold= False)
        
    def __view_Measurement(self, ptwidget, measurement, hold= False):
        '''Show the variable's attributes and a small plot. fix it using the matplotlibwidget
        Using H5 database for ploting measurement signals'''
#             text = 'Name: ' + senyal['unitSymbol']
#             text += '\n' + 'Description: ' + senyal['unitMultiplier']
#             text += '\n' + 'unit: ' + senyal['measurementType']
#             text += '\n' + 'displayUnit: ' + senyal['measurementType']
        ''' TODO updated title, xAxis and yAxis labels
        TODO handle multiple signals- hold option
        TODO export to CSV '''
        ptwidget.theplot.set_title('Something here')
        ptwidget.theplot.set_xlabel('Time (s)')
        ptwidget.theplot.set_ylabel('Magnitude (unit)')
        ptwidget.plot(measurement['sampleTime'], measurement['magnitude'], hold)
        
    def show_meGUI(self):
        modedialog = UI_ModeEstimation(self)
        modedialog.setWindowTitle('Signal Mode Estimation')
        modedialog.show() 

    
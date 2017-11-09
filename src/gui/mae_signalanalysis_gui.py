'''
Created on 19 jan 2016

@author: fragom
'''
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTreeWidgetItem
from inout.streamh5cim import StreamH5CIM
from mae_modeestimation_gui import UI_ModeEstimation
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

__form_gui = uic.loadUiType("./res/mae_signalanalysis_gui.ui")[0] # Load the UI

class UI_SignalAnalysis(QtGui.QDialog, __form_gui):
    __simulation= {}
    __measurement= {}
    __nameSimulationSignal= ''
    __nameMeasurementSignal= ''
    __simudb= None
    __measdb= None

    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
#         self.plotSimu = MatplotlibWidget(self.wgtGraficaSimu, width= 485, height= 380, dpi= 80)
#         self.plotSimu.setGeometry(QtCore.QRect(0, 0, 485, 380))
#         self.plotSimu.setObjectName("mplotSimwidget")
#         self.plotMeas = MatplotlibWidget(self.wgtGraficaMeas, width= 485, height= 380, dpi= 80)
#         self.plotMeas.setGeometry(QtCore.QRect(0, 0, 485, 380))
#         self.plotMeas.setObjectName("mplotMeaswidget")
        self.__createGraficaSimu()
        self.__createGraficaMeas()
        self.toolbars= MultiTabNavTool([self.canvasGS,self.canvasGM],
                                       self.tabWidget, self)
        #vboxtabMeas= QVBoxLayout()
        #vboxtabMeas.addWidget(self.plotMeas)
        #vboxtabMeas.addWidget(self.plotMeas.toolbar)
        
        #
        self.cbxOutputs.activated['QString'].connect(self.__load_OutputSignals)
        self.onLoad_populateOutputFiles()
        #
        self.cbxMeasurements.activated['QString'].connect(self.__load_Measurements)
        self.cbxMeasurements.setEnabled(False)
        # menu items
        self.btnRunAnalysis.clicked.connect(self.show_meGUI)
        self.chbComparewMeas.stateChanged.connect(self.compareWMeas_checked)
        
    def __clearGraficaSimu(self):
        self.graficaGS.clear()
        self.canvasGS.draw()
        
    def __createGraficaSimu(self):
        self.figureGS = plt.figure(figsize=(510, 360), dpi=80)
        self.canvasGS = FigureCanvas(self.figureGS)
#         self.toolbarGS = NavigationToolbar(self.canvasGS, self)
        self.graficaGS = self.figureGS.add_subplot(111) 
        self.graficaGS.grid()
        # set the layout
        layoutGS = QtGui.QFormLayout()
        layoutGS.addWidget(self.canvasGS)
        layoutGS.setContentsMargins(0,0,0,0)
        self.wgtGraficaSimu.setGeometry(QtCore.QRect(0, 0, 510, 410))
        self.wgtGraficaSimu.setLayout(layoutGS)
        
    def __clearGraficaMeas(self):
        self.graficaGM.clear()
        self.canvasGM.draw()
        
    def __createGraficaMeas(self):
        self.figureGM = Figure()
        self.canvasGM = FigureCanvas(self.figureGM)
#         self.toolbarGM = NavigationToolbar(self.canvasGM, self)
        self.graficaGM = self.figureGM.add_subplot(111) 
        self.graficaGM.grid()
        # set the layout
        layoutGM= QtGui.QFormLayout()
        layoutGM.addWidget(self.canvasGM)
        layoutGM.setContentsMargins(0,0,0,0)
        self.wgtGraficaMeas.setGeometry(QtCore.QRect(0, 0, 510, 410))
        self.wgtGraficaMeas.setLayout(layoutGM)
    
    def compareWMeas_checked(self):
        if self.chbComparewMeas.isChecked():
            self.cbxMeasurements.setEnabled(True)
            self.twMeasVariable.setEnabled(True)
            self.onLoad_populateMeasurements()
        else:
            self.cbxMeasurements.setEnabled(False)
            self.twMeasVariable.setEnabled(False)
            self.cbxMeasurements.clear()
        
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
        self.__clearGraficaSimu()
        getSelected = self.twOutVariable.selectedItems()
        for baseNode in getSelected:
            parentName= str(baseNode.parent().text(0))
            childName= baseNode.text(0)
            self.__nameSimulationSignal= parentName+'.'+childName
            if self.__simudb.exist_PowerSystemResource(str(parentName)):
                self.__simudb.select_PowerSystemResource(str(parentName))
                self.__simudb.select_AnalogMeasurement(str(childName))
                self.__simulation= self.__simudb.analogMeasurementValues
                self.__view_Simulation(self.__simudb.analogMeasurementValues)

    def __view_Simulation(self, selectedSignal):
        '''Show the variable's attributes and a small plot. fix it using the matplotlibwidget
        Using H5 database for ploting measurement signals'''
#             text = 'Name: ' + senyal['unitSymbol']
#             text += '\n' + 'Description: ' + senyal['unitMultiplier']
#             text += '\n' + 'unit: ' + senyal['measurementType']
#             text += '\n' + 'displayUnit: ' + senyal['measurementType']
#         ptwidget.plot(measurement['sampleTime'], measurement['magnitude'],
#                       title='Signal', xlabel='Time (s)', ylabel='Magnitude (Unit)', hold= False)
        #for measurement in selectedMeasurement:
        self.graficaGS.plot(selectedSignal['sampleTime'], selectedSignal['magnitude'])
        self.graficaGS.set_title("Signal", fontsize=12)
        self.graficaGS.set_xlabel("Time (s)", fontsize=10)
        self.graficaGS.set_ylabel("Magnitude (Unit)", fontsize=10)
        self.graficaGS.hold(True)
        self.canvasGS.draw()  
        
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
        self.__clearGraficaMeas()
        getSelected = self.twMeasVariable.selectedItems()
        if getSelected== []:
            self.graficaGM.clear()
            self.canvasGM.draw() 
        for baseNode in getSelected:
            parentName= str(baseNode.parent().text(0))
            childName= baseNode.text(0)
            self.__nameMeasurementSignal= parentName+'.'+childName
            if self.__measdb.exist_PowerSystemResource(str(parentName)):
                self.__measdb.select_PowerSystemResource(str(parentName))
                self.__measdb.select_AnalogMeasurement(str(childName))
                self.__measurement= self.__measdb.analogMeasurementValues
                self.__view_Measurement(self.__measdb.analogMeasurementValues)
        
    def __view_Measurement(self, measurement):
        '''Show the variable's attributes and a small plot. fix it using the matplotlibwidget
        Using H5 database for ploting measurement signals'''
#             text = 'Name: ' + senyal['unitSymbol']
#             text += '\n' + 'Description: ' + senyal['unitMultiplier']
#             text += '\n' + 'unit: ' + senyal['measurementType']
#             text += '\n' + 'displayUnit: ' + senyal['measurementType']
#         ptwidget.plot(measurement['sampleTime'], measurement['magnitude'],
#                       title='Signal', xlabel='Time (s)', ylabel='Magnitude (Unit)', hold= False)
        self.graficaGM.plot(measurement['sampleTime'], measurement['magnitude'])
        self.graficaGM.set_title("Signal", fontsize=12)
        self.graficaGM.set_xlabel("Time (s)", fontsize=10)
        self.graficaGM.set_ylabel("Magnitude (Unit)", fontsize=10)
        self.graficaGM.hold(True)
        self.canvasGM.draw()  
        
    def show_meGUI(self):
        modedialog = UI_ModeEstimation(self)
        modedialog.nameSimulationSignal= self.__nameSimulationSignal
        modedialog.nameMeasurementSignal= self.__nameMeasurementSignal
        modedialog.simulationSignal= self.__simulation if not self.__simulation== {} else {}
        modedialog.measurementSignal= self.__measurement if not self.__measurement== {} else {}
        modedialog.setWindowTitle('Signal Mode Estimation')
        modedialog.show() 

class MultiTabNavTool(QtGui.QWidget):
    def __init__(self, canvases, tabs, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.canvases = canvases
        self.tabs = tabs
        self.toolbars = [NavigationToolbar(canvas, parent) for canvas in self.canvases]
        vbox = QtGui.QVBoxLayout()
        for toolbar in self.toolbars:
            vbox.addWidget(toolbar)
        self.setLayout(vbox)
        self.setGeometry(QtCore.QRect(10, 520, 680, 55))
        self.switch_toolbar()
        self.tabs.currentChanged.connect(self.switch_toolbar)

    def switch_toolbar(self):
        for toolbar in self.toolbars:
            toolbar.setVisible(False)
        self.toolbars[self.tabs.currentIndex()].setVisible(True)
            
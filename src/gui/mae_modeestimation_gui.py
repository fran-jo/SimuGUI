'''
Created on 19 jan 2016

@author: fragom
'''

import os
from PyQt4 import QtGui, uic
from PyQt4.QtCore import QString
from methods import MethodAmbientAnalysis
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

__form_gui = uic.loadUiType("./res/mae_modeestimation_gui.ui")[0] # Load the UI

class UI_ModeEstimation(QtGui.QDialog, __form_gui):
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
#         self.plotmodes = MatplotlibWidget(self.mpltgraphic, width= 470, height= 360, dpi= 100,
#                                           xlabel= "Damping", ylabel= "Frequency", title= "Modes")
#         self.plotmodes.setGeometry(QtCore.QRect(0, 0, 470, 360))
        self.createGraficaMeas()
        self.btn_runanalysis.clicked.connect(self.onStart_basicMethod)
        # table of analysis results
        self.tbw_modes.setColumnCount(5)
        self.tbw_modes.setHorizontalHeaderLabels(QString(" ;Sim Freq.;Sim Damp.;Meas Freq..;Meas Damp.").split(";"))
        # unas propertis ahi
        self.__simulation= {}
        self.__measurement= {}
        #
        self.btnClose.clicked.connect(self.closeForm)
        self.chb_meassignal.clicked.connect(self.allowMeasurementSignal)
    
    def createGraficaMeas(self):
        self.figureGM = Figure()
        self.canvasGM = FigureCanvas(self.figureGM)
        self.toolbarGM = NavigationToolbar(self.canvasGM, self)
        self.graficaGM = self.figureGM.add_subplot(111) 
        self.graficaGM.grid()
        # set the layout
        layoutGM = QtGui.QVBoxLayout()
        layoutGM.addWidget(self.canvasGM)
        layoutGM.setContentsMargins(0,0,0,0)
        self.widgetgraphic.setLayout(layoutGM)
        layoutGM = QtGui.QVBoxLayout()
        layoutGM.addWidget(self.toolbarGM)
        layoutGM.setContentsMargins(0,0,0,0)
        self.widgettoolbar.setLayout(layoutGM)
        
    def allowMeasurementSignal(self):
        if self.chb_meassignal.isChecked():
            self.txtNameMeas.setEnabled(True)
        else:
            self.txtNameMeas.setEnabled(False)
            
    @property
    def simulationSignal(self):
        return self.__simulation
    @simulationSignal.setter
    def simulationSignal(self, value):
        self.__simulation= value
    @property
    def measurementSignal(self):
        return self.__measurement
    @measurementSignal.setter
    def measurementSignal(self, value):
        self.__measurement= value
        
    @property
    def nameSimulationSignal(self):
        return self.txtNameSignal.text()
    @nameSimulationSignal.setter
    def nameSimulationSignal(self, value):
        self.txtNameSignal.setText(value)
        
    @property
    def nameMeasurementSignal(self):
        return self.txtNameMeas.text()
    @nameMeasurementSignal.setter
    def nameMeasurementSignal(self, value):
        self.txtNameMeas.setText(value)
        
    def onStart_basicMethod(self):
        self.tbw_modes.setRowCount(0)
        if not self.chb_meassignal.isChecked():
            self.__measurement= {}
        self.__analysisTask = MethodAmbientAnalysis(self.__simulation, self.__measurement)
        self.__analysisTask.order= str(self.txt_modelorder.text())
        self.__analysisTask.toolDir= os.getcwd()
        self.__analysisTask.taskFinished.connect(self.onFinish_basicMethod)
        self.__analysisTask.start()
            
    def onFinish_basicMethod(self):
        os.chdir(self.__analysisTask.toolDir)
        self.__analysisTask.gather_EigenValues()
        xmode= []
        ymode= []
        rowPosition= 0
        for mode in self.__analysisTask.simulationModes:
            rowPosition = self.tbw_modes.rowCount()
            self.tbw_modes.insertRow(rowPosition)
            self.tbw_modes.setItem(rowPosition, 0, QtGui.QTableWidgetItem('Mode '+ str(rowPosition)))
            self.tbw_modes.setItem(rowPosition, 1, QtGui.QTableWidgetItem(str(mode.real)))
            self.tbw_modes.setItem(rowPosition, 2, QtGui.QTableWidgetItem(str(mode.imag)))
            xmode.append(mode.imag)
            ymode.append(mode.real)
#         self.plotmodes.scatter(xmode, ymode, 
#                                xlabel= "Damping", ylabel= "Frequency", title= "Modes", 
#                                c= 'b', marker= 'o')
        self.__view_graficModes(xmode, ymode)
        if self.chb_meassignal.isChecked()== True:
            print "we will compare with measurements"
            rowPosition= 0
            xmode= []
            ymode= []
            for mode in self.__analysisTask.measurementModes:
                self.tbw_modes.setItem(rowPosition, 3, QtGui.QTableWidgetItem(str(mode.real)))
                self.tbw_modes.setItem(rowPosition, 4, QtGui.QTableWidgetItem(str(mode.imag)))
                if rowPosition> self.tbw_modes.rowCount():
                    self.tbw_modes.insertRow(rowPosition)
                rowPosition= rowPosition+ 1
                xmode.append(mode.imag)
                ymode.append(mode.real)
#             self.plotmodes.scatter(xmode, ymode, 
#                                    xlabel= "Damping", ylabel= "Frequency", title= "Modes",
#                                    c= 'r', marker= '+')
            self.__view_graficModes(xmode, ymode)
        self.tbw_modes.show()
    
    def __view_graficModes(self, xmode, ymode):
#         self.grafica.clear()
        self.graficaGM.scatter(xmode,ymode)
        self.graficaGM.set_title("Modes", fontsize=12)
        self.graficaGM.set_xlabel("Damping [p.u.]", fontsize=10)
        self.graficaGM.set_ylabel("Frequency [Hz]", fontsize=10)
        self.graficaGM.grid()
        self.canvasGM.draw()
        
    def closeForm(self):
        self.done(0) 


    
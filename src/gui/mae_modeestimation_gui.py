'''
Created on 19 jan 2016

@author: fragom
'''
'''TODO add a tab page for each source (simulation,measurement) '''
import os
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtCore import QString
from matplotlibwidget import MatplotlibWidget
from methods import MethodAmbientAnalysis

__form_gui = uic.loadUiType("./res/mae_modeestimation_gui.ui")[0] # Load the UI

class UI_ModeEstimation(QtGui.QDialog, __form_gui):
    
    __simulation= None
    __measurement= None
    
    def __init__(self, simsignal, meassignal, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.plotmodes = MatplotlibWidget(self.mpltgraphic, width= 470, height= 360, dpi= 60)
        self.plotmodes.setGeometry(QtCore.QRect(0, 0, 470, 360))
        self.btn_runanalysis.clicked.connect(self.onStart_basicMethod)
        # table of analysis results
        self.tbw_modes.setColumnCount(5)
        self.tbw_modes.setHorizontalHeaderLabels(QString(" ;Sim Freq.;Sim Damp.;Meas Freq..;Meas Damp.").split(";"))
        #
        self.__simulation= simsignal
        self.__measurement= meassignal
        
    def onStart_basicMethod(self):
        self.tbwAnalysisRes.setRowCount(0)
        if not self.chb_meassignal.isChecked():
            self.__measurement= []
        self.__analysisTask = MethodAmbientAnalysis(self.__simulation, self.__measurement)
        self.__analysisTask.order= str(self.txt_modelorder.text())
        self.__analysisTask.toolDir= os.getcwd()
        self.__analysisTask.taskFinished.connect(self.onFinish_basicMethod)
        self.__analysisTask.start()
            
    def onFinish_basicMethod(self):
        os.chdir(self.__analysisTask.toolDir)
        self.__analysisTask.gather_EigenValues()
        rowPosition= 0
        for mode in self.__analysisTask.simulationModes:
            rowPosition = self.tbwAnalysisRes.rowCount()
            self.tbwAnalysisRes.insertRow(rowPosition)
            self.tbwAnalysisRes.setItem(rowPosition, 0, QtGui.QTableWidgetItem('Mode '+ str(rowPosition)))
            self.tbwAnalysisRes.setItem(rowPosition, 1, QtGui.QTableWidgetItem(str(mode.real)))
            self.tbwAnalysisRes.setItem(rowPosition, 2, QtGui.QTableWidgetItem(str(mode.imag)))
        if self.cbx_meassignal.isChecked():
            rowPosition= 0
            for mode in self.__analysisTask.measurementModes:
                self.tbwAnalysisRes.setItem(rowPosition, 3, QtGui.QTableWidgetItem(str(mode.real)))
                self.tbwAnalysisRes.setItem(rowPosition, 4, QtGui.QTableWidgetItem(str(mode.imag)))
                if rowPosition> self.tbwAnalysisRes.rowCount():
                    self.tbwAnalysisRes.insertRow(rowPosition)
                rowPosition= rowPosition+ 1
        self.tbwAnalysisRes.show()
        ''' TODO: first use the mode_estimation_res.h5 directly '''
        ''' TODO: second, use the whole workflow '''
        


    
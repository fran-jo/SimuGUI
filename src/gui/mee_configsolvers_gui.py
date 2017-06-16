'''
Created on Dec 13, 2015

@author: fran_jo
'''
from PyQt4 import QtGui, uic
from ctrl import SimulationConfigOMCDY, SimulationConfigJM
   
form_gui = uic.loadUiType("./res/mee_configsolvers_gui.ui")[0] # Load the UI
                 
class UI_ConfigSolver(QtGui.QDialog, form_gui):
    '''
    classdocs
    '''
    defaultconfigOMC='./config/simConfigurationOMC.properties'
    defaultconfigDY= './config/simConfigurationDY.properties'
    defaultconfigJM= './config/simConfigurationJM.properties'
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        ''' select configuration for simulation '''
        self.rbt_omc.setChecked(True)
        self.cbx_jmAlgorithm.setEnabled(False)
        self.cbx_jmInit.setEnabled(False)
        self.rbt_dy.clicked.connect(self.choose_compiler_selected)
        self.rbt_jm.clicked.connect(self.choose_compiler_selected)
        self.rbt_omc.clicked.connect(self.choose_compiler_selected)
        ''' save/load configuration '''
        self.btnSaveConfig.clicked.connect(self.btn_saveConfig_clicked)
        self.btnLoadConfig.clicked.connect(self.btn_loadConfig_clicked)
    
    ### select compiler and its configuration
    def choose_compiler_selected(self):
        if self.rbt_dy.isChecked() | self.rbt_omc.isChecked():
            self.cbx_jmAlgorithm.setEnabled(False)
            self.cbx_jmInit.setEnabled(False)
        elif self.rbt_jm.isChecked():
            self.cbx_jmAlgorithm.setEnabled(True)
            self.cbx_jmInit.setEnabled(True)
            
    ### save/load configuration
    def btn_loadConfig_clicked(self):
        if self.rbt_dy.isChecked() | self.rbt_omc.isChecked():
            if self.rbt_dy.isChecked():
                self.simconfig=SimulationConfigOMCDY([self.defaultconfigDY,'r+'])
            else:
                self.simconfig= SimulationConfigOMCDY([self.defaultconfigOMC,'r+'])
            self.simconfig.load_Properties()
            self.txt_startTime.setText(self.simconfig.startTime)
            self.txt_stopTime.setText(self.simconfig.stopTime)
            self.txt_interval.setText(self.simconfig.numberOfIntervals)
            self.txt_tolerance.setText(self.simconfig.tolerance)
            # solver and format
            indx= self.cbx_solver.findText(self.simconfig.method)
            if (indx!= -1):
                self.cbx_solver.setCurrentIndex(indx)
            else:
                self.cbx_solver.setItemText(0, self.simconfig.method)
            indx= self.cbx_format.findText(self.simconfig.outputFormat)
            if (indx!= -1):
                self.cbx_format.setCurrentIndex(indx)
            else:
                self.cbx_format.setItemText(0, self.simconfig.outputFormat)
        elif self.rbt_jm.isChecked():
            self.simconfig= SimulationConfigJM([self.defaultconfigJM,'r+'])
                
    def btn_saveConfig_clicked(self):
        if self.rbt_dy.isChecked() | self.rbt_omc.isChecked():
            if self.rbt_dy.isChecked():
                self.simconfig= SimulationConfigOMCDY([self.defaultconfigDY,'w'])
            else:
                self.simconfig= SimulationConfigOMCDY([self.defaultconfigOMC,'w'])
            self.simconfig.startTime= self.txt_startTime.text()
            self.simconfig.stopTime= self.txt_stopTime.text()
            self.simconfig.numberOfIntervals= self.txt_interval.text()
            self.simconfig.tolerance= str(self.cbx_solver.currentText())
            self.simconfig.method= str(self.cbx_format.currentText())
            self.simconfig.outputFormat= self.txt_tolerance.text()
        elif self.rbt_jm.isChecked():
            self.simconfig= SimulationConfigJM([self.defaultconfigJM,'w'])
        self.simconfig.save_Properties()
        
    
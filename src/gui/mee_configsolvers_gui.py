'''
Created on Dec 13, 2015

@author: fran_jo
'''
from PyQt4 import QtGui, uic
from model import DymolaConfiguration, OpenModelicaConfiguration, JModelicaConfiguration
   
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
        self.txtfixstep.setEnabled(False)
        self.rbt_dy.clicked.connect(self.choose_compiler_selected)
        self.rbt_jm.clicked.connect(self.choose_compiler_selected)
        self.rbt_omc.clicked.connect(self.choose_compiler_selected)
        self.chbfixstep.clicked.connect(self.set_step_size)
        ''' save/load configuration '''
        self.btnSaveConfig.clicked.connect(self.btn_saveConfig_clicked)
        self.btnLoadConfig.clicked.connect(self.btn_loadConfig_clicked)
    
    def set_step_size(self):
        self.txtfixstep.setEnabled(True if self.chbfixstep.isChecked() else False)
        self.txtInterval.setEnabled(False if self.chbfixstep.isChecked() else True)
        
    ### select compiler and its configuration
    def choose_compiler_selected(self):
        if self.rbt_dy.isChecked() | self.rbt_omc.isChecked():
            self.cbx_jmAlgorithm.setEnabled(False)
            self.cbx_jmInit.setEnabled(False)
        elif self.rbt_jm.isChecked():
            self.cbx_jmAlgorithm.setEnabled(True)
            self.cbx_jmInit.setEnabled(True)
            
    ### save/load configuration
    def __view_configuration(self):
        self.txtStartTime.setText(self.__simconfig.startTime)
        self.txtStopTime.setText(self.__simconfig.stopTime)
        self.txtInterval.setText(self.__simconfig.numberOfIntervals)
        self.txtfixstep.setText(self.__simconfig.fixStepSize)
        self.txtTolerance.setText(self.__simconfig.tolerance)
        # solver and format
        indx= self.cbxSolver.findText(self.__simconfig.method)
        if (indx!= -1):
            self.cbxSolver.setCurrentIndex(indx)
        else:
            self.cbxSolver.setItemText(0, self.__simconfig.method)
        indx= self.cbxFormat.findText(self.__simconfig.outputFormat)
        if (indx!= -1):
            self.cbxFormat.setCurrentIndex(indx)
        else:
            self.cbxFormat.setItemText(0, self.__simconfig.outputFormat)
    
    def btn_loadConfig_clicked(self):
        if self.rbt_dy.isChecked():
            self.__simconfig=DymolaConfiguration([self.defaultconfigDY,'r+'])
            self.__simconfig.compiler="dymola"
        if self.rbt_omc.isChecked():
            self.__simconfig= OpenModelicaConfiguration([self.defaultconfigOMC,'r+'])
            self.__simconfig.compiler="openmodelica"
        if self.rbt_jm.isChecked():
            self.__simconfig= JModelicaConfiguration([self.defaultconfigJM,'r+'])
            self.__simconfig.compiler="jmodelica"
        self.__simconfig.load_Properties()
        self.__view_configuration()
                 
    def btn_saveConfig_clicked(self):
        if self.rbt_dy.isChecked():
            self.__simconfig= DymolaConfiguration([self.defaultconfigDY,'w'])
            self.__simconfig.compiler= 'dymola'
            self.__simconfig.tolerance= str(self.txtTolerance.text())
            self.__simconfig.method= str(self.cbxSolver.currentText())
            self.__simconfig.outputFormat= str(self.cbxFormat.currentText())
        if self.rbt_omc.isChecked():
            self.__simconfig= OpenModelicaConfiguration([self.defaultconfigOMC,'w'])
            self.__simconfig.compiler= 'openmodelica'
            self.__simconfig.tolerance= str(self.txtTolerance.text())
            self.__simconfig.method= str(self.cbxSolver.currentText())
            self.__simconfig.outputFormat= str(self.cbxFormat.currentText())
        if self.rbt_jm.isChecked():
            self.__simconfig= JModelicaConfiguration([self.defaultconfigJM,'w'])
            self.__simconfig.compiler= 'jmodelica'
            self.__simconfig.solver= str(self.cbxSolver.currentText())
        self.__simconfig.startTime= str(self.txtStartTime.text())
        self.__simconfig.stopTime= str(self.txtStopTime.text())
        if self.chbfixstep.isChecked():
            self.__simconfig.numberOfIntervals= str(-1)
            self.__simconfig.fixStepSize= str(self.txtfixstep.text())
        else:
            self.__simconfig.numberOfIntervals= str(self.txtInterval.text())
            self.__simconfig.fixStepSize= str(-1)
        
        self.__simconfig.save_Properties()
        
    @property
    def simulationConfiguration(self):
        return self.__simconfig
        
    
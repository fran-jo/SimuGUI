'''
Created on Dec 13, 2015

@author: fran_jo
'''

import sys
from PyQt4 import QtGui, uic
from inout.commandOMC import CommandOMC
from OMPython import OMCSession
from inout.ctrlinfogui import SimulationResources, SimulationConfiguration, SimulationConfigJM
   
form_class = uic.loadUiType("./res/mee_simulation_gui.ui")[0] # Load the UI
                 
class SimulationGUI(QtGui.QMainWindow, form_class):
    '''
    classdocs
    TODO: list of components and variables of the model 
    '''
    defaultsourcesFile='./config/simResources.properties'
    defaultconfigOMC='./config/simConfigurationOMC.properties'
    defaultconfigDY= './config/simConfigurationDY.properties'
    defaultconfigJM= './config/simConfigurationJM.properties'
    fname3='ClassNames.properties'
    fname4='ieee9bus_varList.properties'
#     source2=SimulationConfigurationOMC([fname2,'w'])
#     source3=SimulationConfigurationOMC([fname3,'w'])
    modellist=[]
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        ''' select resources for simulation '''
        self.simsource= SimulationResources([self.defaultsourcesFile,'r+'])
        self.btn_loadModelFile.clicked.connect(self.btn_loadModelFile_clicked)  # Bind the event handlers
        self.btn_loadLibraryFile.clicked.connect(self.btn_loadLibraryFile_clicked)  #   to the buttons
        self.btn_loadModel.clicked.connect(self.btn_loadModel_clicked)
        self.btn_loadOutPath.clicked.connect(self.btn_loadOutPath_clicked)
        ''' save/load resources '''
        self.btn_saveResources.clicked.connect(self.btn_saveResources_clicked)
        self.btn_loadResources.clicked.connect(self.btn_loadResources_clicked)
        ''' select configuration for simulation '''
        self.rbt_omc.setChecked(True)
        self.cbx_jmAlgorithm.setEnabled(False)
        self.cbx_jmInit.setEnabled(False)
        self.rbt_dy.clicked.connect(self.choose_compiler_selected)
        self.rbt_jm.clicked.connect(self.choose_compiler_selected)
        self.rbt_omc.clicked.connect(self.choose_compiler_selected)
        ''' save/load configuration '''
        self.btn_saveConfig.clicked.connect(self.btn_saveConfig_clicked)
        self.btn_loadConfig.clicked.connect(self.btn_loadConfig_clicked)
    
    ### select resources for simulation 
    def btn_loadModelFile_clicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Select file')
        if fname:
            self.txt_modelFile.setText(fname)
        else:
            self.txt_modelFile.setText('No file selected!')
            
    def btn_loadLibraryFile_clicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Select file')
        if fname:
            self.txt_libraryFile.setText(fname)
        else:
            self.txt_libraryFile.setText('No file selected!')
            
    def btn_loadModel_clicked(self):
        OMPython = OMCSession()
        command= CommandOMC()
        OMPython.execute(command.loadModelica())
        OMPython.execute(command.loadFile(str(self.txt_modelFile.text())))
        filetouse= str(self.txt_modelFile.text()).split('/')
        modeltouse= filetouse[-1].split('.')[0]
#         print filetouse
#         print modeltouse
        modelNames=OMPython.execute(command.getClassNames(modeltouse))
#         print modelNames['SET1']['Set1']
        fle= open('dict1.properties','w')
        for x in range(len(modelNames['SET1']['Set1'])):
            self.modellist.append(modelNames['SET1']['Set1'][x])
            fle.writelines(str(modelNames['SET1']['Set1'][x]+'\n'))
            # add modellist to combobox
            self.cbx_modelList.addItem(modelNames['SET1']['Set1'][x])

    def btn_loadOutPath_clicked(self):
        outpathname = QtGui.QFileDialog.getExistingDirectory(self, 'Select file')
        if outpathname:
            self.opath=str(outpathname)
            self.txt_outPath.setText(outpathname)
        else:
            self.txt_outPath.setText('No file selected')
    
    ### save/load resources
    def btn_loadResources_clicked(self):
        sourcesFile = QtGui.QFileDialog.getOpenFileName(self, 'Select Resources properties')
        self.simsource= SimulationResources([sourcesFile,'r+'])
        self.simsource.load_Properties()
        self.txt_modelFile.setText(self.simsource.get_modelFile())
        self.txt_libraryFile.setText(self.simsource.get_libraryFile())
        self.txt_outPath.setText(self.simsource.get_outputPath())
        
    def btn_saveResources_clicked(self): 
#         sourcesFile = QtGui.QFileDialog.getOpenFileName(self, 'Select Resources properties')
#         self.simsource= SimulationResources([sourcesFile,'w'])
        ''' processing absolute path of .mo file into path and file '''
        absolutName= str(self.txt_modelFile.text()).split('/')
        mpath='/'.join(absolutName[:-1])
        mfile=''.join(absolutName[-1:])
        self.simsource.set_modelFile(mfile)
        self.simsource.set_modelPath(mpath)
        ''' processing absolute path of .mo file into path and file '''
        absolutName= str(self.txt_libraryFile.text()).split('/')
        mpath='/'.join(absolutName[:-1])
        mfile=''.join(absolutName[-1:])
        self.simsource.set_libraryFile(mfile)
        self.simsource.set_libraryPath(mpath)
        self.simsource.set_modelName(str(self.cbx_modelList.currentText()))
        self.simsource.set_outputPath(str(self.txt_outPath.text()))
        self.simsource.save_Properties()  
         
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
        if self.rbt_dy.isChecked():
            self.simconfig=SimulationConfiguration([self.defaultconfigDY,'r+'])
            self.simconfig.load_Properties()
            self.txt_startTime.setText(self.simconfig.get_starttime())
            self.txt_stopTime.setText(self.simconfig.get_stoptime())
            self.txt_interval.setText(self.simconfig.get_intervals())
            self.txt_tolerance.setText(self.simconfig.get_tolerance())
            # solver and format
            indx= self.cbx_solver.findText(self.simconfig.get_solver())
            if (indx!= -1):
                self.cbx_solver.setCurrentIndex(indx)
            else:
                self.cbx_solver.setItemText(0, self.simconfig.get_solver())
            indx= self.cbx_format.findText(self.simconfig.get_outputformat())
            if (indx!= -1):
                self.cbx_format.setCurrentIndex(indx)
            else:
                self.cbx_format.setItemText(0, self.simconfig.get_outputformat())
        elif self.rbt_jm.isChecked():
            self.simconfig=SimulationConfigJM([self.defaultconfigJM,'r+'])
        elif self.rbt_omc.isChecked():
            self.simconfig=SimulationConfiguration([self.defaultconfigOMC,'r+'])
            self.simconfig.load_Properties()
            self.txt_startTime.setText(self.simconfig.get_starttime())
            self.txt_stopTime.setText(self.simconfig.get_stoptime())
            self.txt_interval.setText(self.simconfig.get_intervals())
            self.txt_tolerance.setText(self.simconfig.get_tolerance())
            # solver and format
            indx= self.cbx_solver.findText(self.simconfig.get_solver())
            if (indx!= -1):
                self.cbx_solver.setCurrentIndex(indx)
            else:
                self.cbx_solver.setItemText(0, self.simconfig.get_solver())
            indx= self.cbx_format.findText(self.simconfig.get_outputformat())
            if (indx!= -1):
                self.cbx_format.setCurrentIndex(indx)
            else:
                self.cbx_format.setItemText(0, self.simconfig.get_outputformat())
            
    def btn_saveConfig_clicked(self):
        if self.rbt_dy.isChecked():
            self.simconfig=SimulationConfiguration([self.defaultconfigDY,'w'])
            self.simconfig.set_starttime(self.txt_startTime.text())
            self.simconfig.set_stoptime(self.txt_stopTime.text())
            self.simconfig.set_intervals(self.txt_interval.text())
            self.simconfig.set_solver(str(self.cbx_solver.currentText()))
            self.simconfig.set_outputformat(str(self.cbx_format.currentText()))
            self.simconfig.set_tolerance(self.txt_tolerance.text())
        if self.rbt_jm.isChecked():
            self.simconfig=SimulationConfigJM([self.defaultconfigJM,'w'])
        if self.rbt_omc.isChecked():
            self.simconfig=SimulationConfiguration([self.defaultconfigOMC,'w'])
            self.simconfig.set_starttime(self.txt_startTime.text())
            self.simconfig.set_stoptime(self.txt_stopTime.text())
            self.simconfig.set_intervals(self.txt_interval.text())
            self.simconfig.set_solver(str(self.cbx_solver.currentText()))
            self.simconfig.set_outputformat(str(self.cbx_format.currentText()))
            self.simconfig.set_tolerance(self.txt_tolerance.text())
        self.simconfig.save_Properties()
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = SimulationGUI(None)
    myWindow.show()
    app.exec_()
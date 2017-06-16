'''
Created on Dec 13, 2015

@author: fran_jo
'''
from PyQt4 import QtGui, uic
from ctrl.ctrlresources import SimulationResources
   
form_gui = uic.loadUiType("./res/mee_loadsources_gui.ui")[0] # Load the UI
                 
class UI_LoadSources(QtGui.QDialog, form_gui):
    '''
    classdocs
    '''
    defaultsourcesFile='./config/simResources.properties'
    modellist=[]
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        ''' select resources for simulation '''
        self.simsource= SimulationResources([self.defaultsourcesFile,'r+'])
        self.btnCIMFolder.clicked.connect(lambda: self.load_folderPath(1))
        self.btnModelFolder.clicked.connect(lambda: self.load_folderPath(2)) 
        self.btnLibraryFolder.clicked.connect(lambda: self.load_folderPath(3))  
        self.btnOutputsFolder.clicked.connect(lambda: self.load_folderPath(4))
        ''' save/load resources '''
        self.btn_saveResources.clicked.connect(self.btn_saveResources_clicked)
        self.btn_loadResources.clicked.connect(self.btn_loadResources_clicked)
    
    ### select resources for simulation 
    def load_folderPath(self, txt):
        carpetaName = QtGui.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if (txt== 1):
            if carpetaName:
                self.txtCIMFolder.setText(carpetaName)
            else:
                self.txtCIMFolder.setText('No file selected!')
        if (txt== 2):
            if carpetaName:
                self.txtModelsFolder.setText(carpetaName)
            else:
                self.txtModelsFolder.setText('No file selected!')
        if (txt== 3):
            if carpetaName:
                self.txtLibraryFolder.setText(carpetaName)
            else:
                self.txtLibraryFolder.setText('No file selected!')
        if (txt== 4):
            if carpetaName:
                self.txtOutputFolder.setText(carpetaName)
            else:
                self.txtOutputFolder.setText('No file selected!')
    
    ### save/load resources
    def btn_loadResources_clicked(self):
        sourcesFile = QtGui.QFileDialog.getOpenFileName(self, 'Select Resources properties')
        self.simsource= SimulationResources([sourcesFile,'r+'])
        self.simsource.load_Properties()
        self.txtCIMFolder.setText(self.simsource.cimfolder)
        self.txtModelsFolder.setText(self.simsource.modelfolder)
        self.txtLibraryFolder.setText(self.simsource.libraryfolder)
        self.txtOutputFolder.setText(self.simsource.outputfolder)
        
    def btn_saveResources_clicked(self): 
#         sourcesFile = QtGui.QFileDialog.getOpenFileName(self, 'Select Resources properties')
#         self.simsource= SimulationResources([sourcesFile,'w'])
        ''' processing absolute path of .mo file into path and file '''
        self.simsource.cimfolder= str(self.txtCIMFolder.text())
        self.simsource.modelfolder= str(self.txtModelsFolder.text())
        self.simsource.libraryfolder= str(self.txtLibraryFolder.text())
        self.simsource.outputfolder= str(self.txtOutputFolder.text())
        self.simsource.save_Properties()  
        
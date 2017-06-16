'''
Created on Dec 13, 2015

@author: fran_jo
'''

from PyQt4 import QtGui, uic
from ctrl import SimulationResources
   
form_sources = uic.loadUiType("./res/mee_loadsources.ui")[0] # Load the UI
                 
class UI_LoadSources(QtGui.QDialog, form_sources):
    '''
    classdocs
    '''
    defaultsourcesFile='./config/simResources.properties'
    modellist=[]
    
    def __init__(self):
        super(self.__class__, self).__init__()
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
            
#     def btn_loadModel_clicked(self):
#         OMPython = OMCSession()
#         command= CommandOMC()
#         OMPython.execute(command.loadModelica())
#         OMPython.execute(command.loadFile(str(self.txt_modelFile.text())))
#         filetouse= str(self.txt_modelFile.text()).split('/')
#         modeltouse= filetouse[-1].split('.')[0]
# #         print filetouse
# #         print modeltouse
#         modelNames=OMPython.execute(command.getClassNames(modeltouse))
# #         print modelNames['SET1']['Set1']
#         fle= open('dict1.properties','w')
#         for x in range(len(modelNames['SET1']['Set1'])):
#             self.modellist.append(modelNames['SET1']['Set1'][x])
#             fle.writelines(str(modelNames['SET1']['Set1'][x]+'\n'))
#             # add modellist to combobox
#             self.cbx_modelList.addItem(modelNames['SET1']['Set1'][x])
    
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
         
    
# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     myWindow = SimulationGUI(None)
#     myWindow.show()
#     app.exec_()
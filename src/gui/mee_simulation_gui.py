'''
Created on Dec 13, 2015

@author: fran_jo
'''

import sys
from PyQt4 import QtCore, QtGui, uic
from commandOMC import CommandOMC
from OMPython import OMCSession
from ctrlinfogui import SimulationResources

form_class = uic.loadUiType("./res/mee_simulation_gui.ui")[0] # Load the UI
                 
class SimulationGUI(QtGui.QMainWindow, form_class):
    '''
    classdocs
    '''
    li1=[]
    _fileName=""
    _MN=""
    newItem=""
    mpath=""
    lpath=""
    mfile=""
    mname=""
    lfile=""
    opath=""
    fname1='simParametersOMC4.properties'
    fname2='simConfigurationOMC3.properties'
    fname3='ClassNames.properties'
    fname4='ieee9bus_varList.properties'
#     source2=SimulationConfigurationOMC([fname2,'w'])
#     source3=SimulationConfigurationOMC([fname3,'w'])
    modellist=[]
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        ''' select resources for simulation '''
        self.btn_loadModelFile.clicked.connect(self.btn_loadModelFile_clicked)  # Bind the event handlers
        self.btn_loadLibraryFile.clicked.connect(self.btn_loadLibraryFile_clicked)  #   to the buttons
        self.btn_loadModel.clicked.connect(self.btn_loadModel_clicked)
        self.btn_loadOutPath.clicked.connect(self.btn_loadOutPath_clicked)
        ''' save/load resources '''
        self.btn_saveResources.clicked.connect(self.btn_saveResources_clicked)
        self.btn_loadResources.clicked.connect(self.btn_loadResources_clicked)
    
    ''' select resources for simulation '''
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
        OMPython.execute(command.loadFile(self.mfile))
        #print self.mfile
        #print command.set_ModelName(self.mfile)
        self._MN=OMPython.execute(command.getClassNames(self.mfile))
        self.filetouse=self.mfile.replace('.mo', '.')
        print self._MN['SET1']['Set1']
        fle= open('dict1.properties','w')
        for x in range(len(self._MN['SET1']['Set1'])):
            self.modellist.append(self.filetouse+self._MN['SET1']['Set1'][x])
            fle.writelines(str(self.filetouse+self._MN['SET1']['Set1'][x]+'\n'))

    def btn_loadOutPath_clicked(self):
        self.fname = QtGui.QFileDialog.getExistingDirectory(self, 'Select file')
        if self.fname:
            self.opath=str(self.fname)
            self.txt_outPath.setText(self.opath)
        else:
            self.txt_outPath.setText('No file selected')
    
    ''' save/load resources '''
    def btn_loadResources_clicked(self):
        sourcesFile = QtGui.QFileDialog.getOpenFileName(self, 'Select Resources properties')
        self.simsource= SimulationResources([sourcesFile,'r+'])
        self.simsource.load_Properties()
        self.txt_modelFile.setText(self.simsource.get_modelFile())
        #print self.sources.get_modelFile()
        self.txt_libraryFile.setText(self.simsource.get_libraryFile())
        #self.lineEdit_3.setText(self.sources.get_modelName())
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
        self.simsource.set_libraryFile(mpath)
        self.simsource.set_libraryPath(mfile)
        self.simsource.set_modelName(str(self.cbx_modelList.currentText()))
        self.simsource.set_outputPath(self.txt_outPath.text())
        self.simsource.save_Properties()  
         
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = SimulationGUI(None)
    myWindow.show()
    app.exec_()
'''
Created on Dec 13, 2015

@author: fran_jo
'''
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QIcon
from OMPython import OMCSession
from classes import CommandOMC
from engines.engineOpenModelica import EngineOMC
from engines.engineDymola import EngineDY
from modelicares import SimRes
from gui.mee_plot_gui import UI_Plot_MEE
# from gui import msv_plot_gui
   
form_gui = uic.loadUiType("./res/mee_simulation_gui.ui")[0] # Load the UI
                 
class UI_Simulation(QtGui.QDialog, form_gui):
    '''
    classdocs
    TODO: list of components and variables of the model 
    '''
    __engine= None 
    __results= None
    
    def __init__(self, parent= None, configResources= None, configSimulation= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__simsource= configResources
        self.__simconfig= configSimulation
        self.load_configuration()
        self.btnModelBrowser.clicked.connect(self.browse_models)
        self.btnLibraryBrowser.clicked.connect(self.browse_libraries)
        self.cbxModelList.activated['QString'].connect(self.set_models)
        self.progressBar.setRange(0,1)
        #
        self.btnRunSimulation.setIcon(QIcon('./res/img/Play.ico'))
        self.btnRunSimulation.setIconSize(QSize(48,48))
        self.btnRunSimulation.clicked.connect(self.onStartSimulation)
        self.btnPlot.setIcon(QIcon('./res/img/Presentation.ico'))
        self.btnPlot.setIconSize(QSize(48,48))
        self.btnPlot.clicked.connect(self.browse_simulation)
        #debug
        self.__omcSession= OMCSession()
        if self.__simconfig.compiler== 'dymola':
            self.__simulationTask = TaskThreadDY(self, self.__simsource, self.__simconfig, self.__results)
        elif self.__simconfig.compiler== 'jmodelica':
            pass
        elif self.__simconfig.compiler== 'openmodelica':
            self.__simulationTask = TaskThreadOMC(self, self.__simsource, self.__simconfig, self.__omcSession, self.__results)
        self.__simulationTask.taskFinished.connect(self.onFinishSimulation)
    
    ### save/load configuration
    def load_configuration(self):
        if self.__simconfig!= None:
            self.txtCompiler.setText(self.__simconfig.compiler)
            self.txtStartTime.setText(self.__simconfig.startTime)
            self.txtStopTime.setText(self.__simconfig.stopTime)
            self.txtInterval.setText(self.__simconfig.numberOfIntervals)
            self.txtTolerance.setText(self.__simconfig.tolerance)
            self.txtSolver.setText(self.__simconfig.method)
            
    def browse_models(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open Model file', 
                                                     directory= self.__simsource.modelFolder+'/', 
                                                     filter='Modelica Models (*.mo)')
        self.txtModelFile.setText(fileName)
        self.__simsource.modelFile= str(fileName)
        self.__simsource.modelName= str(fileName)
        self.cbxModelList.clear()
        command= CommandOMC()
        success= self.__omcSession.execute(command.loadFile(self.__simsource.modelFile))
        if (success):
            modelNames= self.__omcSession.execute(command.getClassNames(self.__simsource.modelName))
#             print modelNames
#             print modelNames['SET1']['Set1'][0]
    #         fle= open('dict1.properties','w')
            for x in range(len(modelNames['SET1']['Set1'])):
    #             self.modellist.append(modelNames['SET1']['Set1'][x])
    #             fle.writelines(str(modelNames['SET1']['Set1'][x]+'\n'))
                # add modellist to combobox
                self.cbxModelList.addItem(modelNames['SET1']['Set1'][x])
        else:
            print 'Something unexpected happened!'
     
    def set_models(self, text):
        self.__simconfig.modelName= str(text)
        
    def browse_libraries(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open Library file', 
                                                     directory= self.__simsource.libraryFolder+'/', 
                                                     filter='Modelica Models (*.mo)')
        self.txtLibraryFile.setText(fileName)
        self.__simsource.libraryFile= str(fileName)
        
    def browse_simulation(self):
#         simmodel = SimRes('./SevenBus.Network_res.mat')
        #debug
        ''' TODO change debug object, use simulation results '''
        simmodel = SimRes('./res/dy/Two_Areas_PSSE_AVR_Noise_dassl_dsin.mat')
#         simmodel.browse()
        simbrowser = UI_Plot_MEE(self, simmodel)
        simbrowser.show() 
    
    def onStartSimulation(self):
        self.progressBar.setRange(0,0)
        self.__simulationTask.start()
            
    def onFinishSimulation(self):
        # Stop the pulsation
        self.progressBar.setRange(0,100)
    
    def closeEvent(self, event):
        self.__omcSession.sendExpression('quit()')
        self.__omcSession= None
        event.accept() # let the window close
   
class TaskThreadDY(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()
    
    def __init__(self, parent= None, sources= None, experiment= None, results= None):
        QtCore.QThread.__init__(self, parent)
        self.__simsources= sources
        self.__experiment= experiment
        self.__results= results
        
    def run(self):
        print 'DY Thread'
        simCity= EngineDY(self.__simsources, self.__experiment, self.__results)
        '''TODO: this function must store the result file in the proper folder '''
        simCity.simulate() 
        self.taskFinished.emit()  
        
class TaskThreadJM(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()
    
    def __init__(self, parent= None, sources= None, experiment= None, results= None):
        QtCore.QThread.__init__(self, parent)
        self.__sources= sources
        self.__experiment= experiment
        self.__results= results
        
    def run(self):
        print 'JM Thread'
        self.taskFinished.emit()  
             
class TaskThreadOMC(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()
    
    def __init__(self, parent= None, sources= None, experiment= None, omcConnection= None, results= None):
        QtCore.QThread.__init__(self, parent)
        self.__simsources= sources
        self.__experiment= experiment
        self.__omcSession= omcConnection
        self.__results= results
        
    def run(self):
        print 'OMC Thread'
        simCity= EngineOMC(self.__simsources, self.__experiment, self.__omcSession, self.__results)
        '''TODO: this function must store the result file in the proper folder '''
        simCity.simulate() 
        self.taskFinished.emit()  

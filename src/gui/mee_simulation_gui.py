'''
Created on Dec 13, 2015

@author: fran_jo
'''

import sys
from PyQt4 import QtGui, uic
from ctrl.commandOMC import CommandOMC
from OMPython import OMCSession
from ctrl.ctrlinfogui import SimulationResources, SimulationConfiguration, SimulationConfigJM
   
form_gui = uic.loadUiType("./res/mee_simulation_gui.ui")[0] # Load the UI
                 
class UI_Simulation(QtGui.QDialog, form_gui):
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
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        ''' save/load configuration '''
        self.btnModelBrowser.clicked.connect(self.browse_models)
        self.btnRunSimulation.clicked.connect(self.simulate_model)
    
            
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
            
    def browse_models(self):
        pass
    
    ### simulation 
    def simulate_model(self):
        pass
    
    
'''
Created on 19 jan 2016

@author: fragom
'''

import sys
from PyQt4 import QtGui, uic
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QApplication, QIcon
from gui import UI_LoadSources, UI_ConfigSolver, UI_Simulation, UI_Plot_MEE, UI_Plot_MAE, UI_M2M, UI_SignalAnalysis
from modelicares import SimRes
#debug
from ctrl import SimulationResources
from ctrl import SimulationConfigOMCDY

main_form = uic.loadUiType("./res/msv_framework_gui.ui")[0] # Load the UI
# form_confSolver = uic.loadUiType("./res/mee_configsolvers_gui.ui")[0] # Load the UI
form_simulate = uic.loadUiType("./res/mee_simulation_gui.ui")[0] # Load the UI

class MVSGUI(QtGui.QMainWindow, main_form):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #
        self.btnM2M.setIcon(QIcon('./res/img/m2m_transparent.ico'))
        self.btnM2M.setIconSize(QSize(48,48))
        self.btnM2M.clicked.connect(self.m2mDialog)
        #
        self.btnLoadResources.setIcon(QIcon('./res/img/OpenFolder.ico'))
        self.btnLoadResources.setIconSize(QSize(48,48))
        self.btnLoadResources.clicked.connect(self.loadSourcesDialog)
        #
        self.btnConfigSolver.setIcon(QIcon('./res/img/Settings.ico'))
        self.btnConfigSolver.setIconSize(QSize(48,48))
        self.btnConfigSolver.clicked.connect(self.configSolversDialog)
        #
        self.btnSimulate.setIcon(QIcon('./res/img/Play.ico'))
        self.btnSimulate.setIconSize(QSize(48,48))
        self.btnSimulate.clicked.connect(self.simulateDialog)
        #
        self.btnPlotSimu.setIcon(QIcon('./res/img/Presentation.ico'))
        self.btnPlotSimu.setIconSize(QSize(48,48))
        self.btnPlotSimu.clicked.connect(self.plotSimulation)
        self.btnPlotMesurements.setIcon(QIcon('./res/img/Presentation.ico'))
        self.btnPlotMesurements.setIconSize(QSize(48,48))
        self.btnPlotMesurements.clicked.connect(self.plotMeasurements)
        #
        self.btnAnalysis.setIcon(QIcon('./res/img/Gnome_Spreadsheet.ico'))
        self.btnAnalysis.setIconSize(QSize(48,48))
        self.btnAnalysis.clicked.connect(self.signalAnalysis)
        #
        self.btnReport.setIcon(QIcon('./res/img/Presentation.ico'))
        self.btnReport.setIconSize(QSize(64,64))
        self.btnReport.clicked.connect(self.signalAnalysis)
    
    def m2mDialog(self, checked=None):
        if checked== None: return
        self.model2modelDialog = UI_M2M(self)
        self.model2modelDialog.show()
        
    def loadSourcesDialog(self, checked=None):
        if checked== None: return
        self.sourcesDialog = UI_LoadSources(self)
        self.sourcesDialog.show()
        
    def configSolversDialog(self, checked=None):
        if checked== None: return
        self.configSolver = UI_ConfigSolver(self)
        self.configSolver.show()
        
    def simulateDialog(self, checked=None):
        if checked== None: return
        #debug
        ''' TODO change debug object, use loaded configurations '''
#         self.simulationDialog = UI_Simulation(
#             self, SimulationResources(['./config/simResources.properties','r+']), 
#             SimulationConfigOMCDY(['./config/simConfigurationOMC.properties','w']))
        self.simulattionDialog = UI_Simulation(self, self.sourcesDialog.simulationResources, 
                                               self.configSolver.simulationConfiguration)
        self.simulationDialog.show()
        
    def plotSimulation(self, checked=None):
        if checked== None: return
        #debug
        simmodel = SimRes('./res/dy/Two_Areas_PSSE_AVR_Noise_dassl_dsin.mat')
#         simmodel.browse()
        simbrowser = UI_Plot_MEE(self, simmodel)
        simbrowser.setWindowTitle('Simulations')
        simbrowser.show() 
    
    def plotMeasurements(self, checked=None):
        if checked== None: return
        #debug
        ''' TODO change debug object, use simulation results '''
#         measmodel = SimRes('./res/dy/Two_Areas_PSSE_AVR_Noise_dassl_dsin.mat')
#         simmodel.browse()
        measbrowser = UI_Plot_MAE(self)
        measbrowser.setWindowTitle('Measurements')
        measbrowser.show() 
        
    def signalAnalysis(self, checked=None):
        if checked== None: return
        windialog = UI_SignalAnalysis(self)
        windialog.setWindowTitle('Signal Analysis')
        windialog.show() 
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MVSGUI()
    myapp.show()
    sys.exit(app.exec_())
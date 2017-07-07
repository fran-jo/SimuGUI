'''
Created on 19 jan 2016

@author: fragom
'''

import sys
from PyQt4 import QtGui, uic
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QApplication, QIcon
from gui import UI_LoadSources, UI_ConfigSolver, UI_Simulation, UI_Plot, UI_M2M
from modelicares import SimRes

main_form = uic.loadUiType("./res/msv_framework_gui.ui")[0] # Load the UI
# form_confSolver = uic.loadUiType("./res/mee_configsolvers_gui.ui")[0] # Load the UI
form_simulate = uic.loadUiType("./res/mee_simulation_gui.ui")[0] # Load the UI
form_plot = uic.loadUiType("./res/msv_plot_gui.ui")[0] # Load the UI

class MVSGUI(QtGui.QMainWindow, main_form):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #
        self.btnM2M.setIcon(QIcon('./res/img/Settings.ico'))
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
        self.simulattionDialog = UI_Simulation(self, self.sourcesDialog.simulationResources, 
                                               self.configSolver.simulationConfiguration)
        self.simulattionDialog.show()
        
    def plotSimulation(self, checked=None):
        if checked== None: return
        simmodel = SimRes('./res/dy/Two_Areas_PSSE_AVR_Noise_dassl_dsin.mat')
#         simmodel.browse()
        simbrowser = UI_Plot(self, simmodel)
        simbrowser.show() 
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MVSGUI()
    myapp.show()
    sys.exit(app.exec_())
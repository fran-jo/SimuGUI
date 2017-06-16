'''
Created on 19 jan 2016

@author: fragom
'''

import sys, os, subprocess
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QApplication, QDialog
from gui import UI_LoadSources, UI_ConfigSolver, UI_Simulation

main_form = uic.loadUiType("./res/msv_framework_gui.ui")[0] # Load the UI
# form_confSolver = uic.loadUiType("./res/mee_configsolvers_gui.ui")[0] # Load the UI
form_simulate = uic.loadUiType("./res/mee_simulation_gui.ui")[0] # Load the UI
form_plot = uic.loadUiType("./res/msv_plot_gui.ui")[0] # Load the UI

        
# class UI_ConfigSolvers(QtGui.QDialog, form_confSolver):
#     def __init__(self, parent= None):
#         QtGui.QDialog.__init__(self)
        
# class UI_Simulation(QtGui.QDialog, form_simulate):
#     def __init__(self, parent= None):
#         QtGui.QDialog.__init__(self)
        
class UI_Plot(QtGui.QDialog, form_plot):
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self)
        
class MVSGUI(QtGui.QMainWindow, main_form):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
#         self.setWindowTitle("Mode Estimation!")
        self.btnLoadResources.clicked.connect(self.loadSourcesDialog)
        self.btnConfigSolver.clicked.connect(self.configSolversDialog)
        self.btnSimulate.clicked.connect(self.simulateDialog)
        self.btnPlotSimu.clicked.connect(self.plot_btn)
    
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
        self.simulattionDialog = UI_Simulation(self)
        self.simulattionDialog.show()
        
    def plot_btn(self, checked=None):
        if checked== None: return
        dialog = QDialog()
        dialog.ui = UI_Plot()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MVSGUI()
    myapp.show()
    sys.exit(app.exec_())
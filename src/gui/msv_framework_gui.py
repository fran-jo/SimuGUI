'''
Created on 19 jan 2016

@author: fragom
'''

import sys, os, subprocess
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QApplication, QDialog
from mee_loadresources_gui import UI_LoadSources

main_form = uic.loadUiType("./res/msv_framework_gui.ui")[0] # Load the UI
# form_sources = uic.loadUiType("./res/mee_loadsources.ui")[0] # Load the UI
form_confSolver = uic.loadUiType("./res/mee_configsolvers.ui")[0] # Load the UI
form_simulate = uic.loadUiType("./res/mee_simulation.ui")[0] # Load the UI
form_plot = uic.loadUiType("./res/msv_plot_gui.ui")[0] # Load the UI

# class UI_LoadSources(QtGui.QDialog, form_sources):
#     def __init__(self, parent= None):
#         QtGui.QDialog.__init__(self)


class UI_ConfigSolvers(QtGui.QDialog, form_confSolver):
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self)


class UI_Simulation(QtGui.QDialog, form_simulate):
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self)


class UI_Plot(QtGui.QDialog, form_plot):
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self)


class MVSGUI(QtGui.QMainWindow, main_form):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
#         self.setWindowTitle("Mode Estimation!")
        self.btnLoadResources.clicked.connect(self.loadSources_btn)
        self.btnConfigSolver.clicked.connect(self.configSolvers_btn)
        self.btnSimulate.clicked.connect(self.simulate_btn)
        self.btnPlotSimu.clicked.connect(self.plot_btn)
    
    def loadSources_btn(self, checked=None):
        if checked== None: return
        dialog = UI_LoadSources()
        dialog.show()
        
    def configSolvers_btn(self, checked=None):
        if checked== None: 
            return
        dialog = QDialog()
        dialog.ui = UI_ConfigSolvers()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        
    def simulate_btn(self, checked=None):
        if checked== None: return
        dialog = QDialog()
        dialog.ui = UI_Simulation()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        
    def plot_btn(self, checked=None):
        if checked== None: return
        dialog = QDialog()
        dialog.ui = UI_Plot()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MVSGUI()
    myapp.show()
    sys.exit(app.exec_())
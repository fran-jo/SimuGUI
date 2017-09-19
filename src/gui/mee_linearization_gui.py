'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import QSize, QProcess

form_gui = uic.loadUiType("./res/mee_linearization_gui.ui")[0] # Load the UI

class UI_Linearization(QtGui.QDialog, form_gui):
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.load_configuration()
        self.btnModelBrowser.clicked.connect(self.browse_models)
        self.btnLibraryBrowser.clicked.connect(self.browse_libraries)
    
    ### save/load configuration
    def load_configuration(self):
        if self.__simconfig!= None:
            self.txtCompiler.setText(self.__simconfig.compiler)
            self.txtStartTime.setText(self.__simconfig.startTime)
            self.txtStopTime.setText(self.__simconfig.stopTime)
            self.txtInterval.setText(self.__simconfig.numberOfIntervals)
            self.txtTolerance.setText(self.__simconfig.tolerance)
            self.txtSolver.setText(self.__simconfig.method)
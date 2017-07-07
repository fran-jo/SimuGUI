'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import QSize

form_gui = uic.loadUiType("./res/msv_m2m_gui.ui")[0] # Load the UI

class UI_M2M(QtGui.QDialog, form_gui):
    
    __results= None
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        #
        self.btnToModelica.setIcon(QIcon('./res/img/Settings.ico'))
        self.btnToModelica.setIconSize(QSize(48,48))
        self.btnToModelica.clicked.connect(self.cim2modelica)
        
    def cim2modelica(self):
        pass
    
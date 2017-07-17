'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import QSize, QProcess

form_gui = uic.loadUiType("./res/msv_m2m_gui.ui")[0] # Load the UI

class UI_M2M(QtGui.QDialog, form_gui):
    
    __results= None
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.btnBrowseEQ.clicked.connect(lambda: self.loadProfile('EQ'))
        self.btnBrowseTP.clicked.connect(lambda: self.loadProfile('TP'))
        self.btnBrowseSV.clicked.connect(lambda: self.loadProfile('SV'))
        self.btnBrowseDY.clicked.connect(lambda: self.loadProfile('DY'))
        #
        self.btnToModelica.setIcon(QIcon('./res/img/Settings.ico'))
        self.btnToModelica.setIconSize(QSize(48,48))
        self.btnToModelica.clicked.connect(self.cim2modelica)
        #
        self.btnEditModel.setIcon(QIcon('./res/img/Settings.ico'))
        self.btnEditModel.setIconSize(QSize(48,48))
        self.btnEditModel.setEnabled(False)
        self.btnEditModel.clicked.connect(self.browseModels)
        #
#         self.cbxCimSchema.activated['QString'].connect(self.set_models)
        
    def loadProfile(self, cimProfile):
        profileFile = QtGui.QFileDialog.getOpenFileName(self, 'Select CIM Profiles')
        if cimProfile== 'EQ':
            self.txtEQ.setText(profileFile)
        elif cimProfile== 'TP':
            self.txtTP.setText(profileFile)
        elif cimProfile== 'SV':
            self.txtSV.setText(profileFile)
        elif cimProfile== 'DY':
            self.txtDY.setText(profileFile)
        
    def cim2modelica(self):
        command = "java"
        args =  ["-jar", "./lib/cim2modelica.jar",
                 self.txtEQ.text(), self.txtTP.text(), self.txtSV.text(), self.txtDY.text(),
                 self.txtModelName.text(), str(self.cbxCimSchema.currentText())]
        process = QProcess(self)
        process.finished.connect(self.onFinished)
        process.start(command, args)
        
    def onFinished(self):
        print "M2M finished!"
        self.btnEditModel.setEnabled(True)
        
    def browseModels(self):
        dir_to_show = './model/'+ self.txtModelName.text()
        process = QProcess(self)
        process.startDetached("open", [dir_to_show])
        if process.waitForFinished():
            process.close()
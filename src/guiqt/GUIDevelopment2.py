# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIDevelopment.ui'
#
# Created: Wed Sep 23 11:04:38 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from OMPython import OMCSession
import csv
from SimulationOMC import SimulationOMC

 
#from SimulationResources import SimulationResources
#from tstctrl import SimulationResources
from ctrlinfogui import SimulationResources, SimulationConfigurationOMC
from commandOMC import CommandOMC
import sys, time 
import ast

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
   
    li1=[]
    _fileName=""
    time
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
    source1=SimulationResources([fname1,'w'])
    source2=SimulationConfigurationOMC([fname2,'w'])
    source3=SimulationConfigurationOMC([fname3,'w'])
    lis=[]
    
   
    
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(479, 585)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        #self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        #self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.comboBox_5 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_5, 2, 2, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 4, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_2.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_2.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 3, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.gridLayout_2.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_2.addWidget(self.lineEdit_7, 4, 1, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_3, 6, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_2, 3, 3, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_2.addWidget(self.lineEdit_8, 5, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox, 3, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 6, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_2.addWidget(self.pushButton_6, 7, 0, 1, 2)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_4, 6, 3, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_2.addWidget(self.pushButton_7, 7, 2, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout.addWidget(self.pushButton_8)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 10)
        self.progressBar.setMinimum(1)
        self.progressBar.setMaximum(101)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Resources panel", None))
        self.pushButton_4.setText(_translate("Dialog", "Output Path", None))
        self.pushButton_4.clicked.connect(self.Output_path)
        self.label.setText(_translate("Dialog", "Model File", None))
        self.pushButton.setText(_translate("Dialog", "Load Model", None))
        """ calling function for load model"""
        self.pushButton.clicked.connect(self.Load_Model)
        self.label_4.setText(_translate("Dialog", "Output Path", None))
        self.label_2.setText(_translate("Dialog", "Library File", None))
        self.label_3.setText(_translate("Dialog", "Model Name", None))
        self.pushButton_3.setText(_translate("Dialog", "Select Model", None))
        """ function calling for select model"""
        self.pushButton_3.clicked.connect(self.Select_Model)
        self.pushButton_2.setText(_translate("Dialog", "Load Library", None))
        """function calling for Load Library"""
        self.pushButton_2.clicked.connect(self.Load_Library)
        self.pushButton_9.setText(_translate("Dialog", "Save Resources", None))
        self.pushButton_9.clicked.connect(self.get_fname_save_Resource)
        self.pushButton_5.setText(_translate("Dialog", "Load Resources", None))
        """ calling function for load model"""
        self.pushButton_5.clicked.connect(self.Load_Resource)
        self.groupBox.setTitle(_translate("Dialog", "Configuration panel", None))
        self.radioButton_2.setText(_translate("Dialog", "JModelica", None))
        self.radioButton.setText(_translate("Dialog", "OpenModelica", None))
        self.label_5.setText(_translate("Dialog", "Start time", None))
        self.label_6.setText(_translate("Dialog", "Stop time", None))
        self.label_8.setText(_translate("Dialog", "Algorithm(JM)", None))
        self.label_7.setText(_translate("Dialog", "Solver", None))
        self.radioButton_3.setText(_translate("Dialog", "Dymola", None))
        self.label_10.setText(_translate("Dialog", "Tolerance", None))
        self.comboBox_3.setItemText(0, _translate("Dialog", ".mat", None))
        self.comboBox_3.setItemText(1, _translate("Dialog", "New Item", None))
        self.comboBox_3.setItemText(2, _translate("Dialog", "New Item2", None))
        self.label_9.setText(_translate("Dialog", "Interval", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "AssimuloAlg", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "New Item", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", "New Item2", None))
        self.comboBox.setItemText(0, _translate("Dialog", "dassel", None))
        self.comboBox.setItemText(1, _translate("Dialog", "New Item", None))
        self.comboBox.setItemText(2, _translate("Dialog", "New Item2", None))
        self.label_12.setText(_translate("Dialog", "Initialize(JM)", None))
        self.label_11.setText(_translate("Dialog", "Output format", None))
        self.pushButton_6.setText(_translate("Dialog", "Save Configuration", None))
        """calling function for Save Configuration """
        self.pushButton_6.clicked.connect(self.get_save_Configuration)
        #self.pushButton_6.clicked.connect(self.extra)
        self.comboBox_4.setItemText(0, _translate("Dialog", "True", None))
        self.comboBox_4.setItemText(1, _translate("Dialog", "False", None))
        self.pushButton_7.setText(_translate("Dialog", "Load Configuration", None))
        """calling function for Load configuration """
        self.pushButton_7.clicked.connect(self.get_Load_Configuration)
        self.pushButton_8.setText(_translate("Dialog", "Simulate", None))
        self.pushButton_8.clicked.connect(self.Simulation)
    
    """ function for 'Load model'   """
    def Load_Model(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(Dialog, 'Select file')
        if self.fname:
            self.MF=str(self.fname).split('/')
            self.directori='/'.join(self.MF[:-1])
            self.filename=''.join(self.MF[-1:])
            self.mpath=str(self.directori)
            self.mfile=self.filename
            self.lineEdit.setText(self.fname)
            
        else:
            self.lineEdit.setText('No file selected!')
    """ function for 'load Library'    """
    def Load_Library(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(Dialog, 'Select file')
        if self.fname:
            self.MF=str(self.fname).split('/')
            self.directori='/'.join(self.MF[:-1])
            self.source1.set_libraryPath(self.directori)
            self.filename=''.join(self.MF[-1:])
            self.lpath=str(self.directori)
            self.lfile=self.filename
            self.lineEdit_2.setText(self.fname)
        else:
            self.lineEdit_2.setText('No file selected!')
    """ function for 'select model'"""
    def Select_Model(self):
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
            self.lis.append(self.filetouse+self._MN['SET1']['Set1'][x])
            fle.writelines(str(self.filetouse+self._MN['SET1']['Set1'][x]+'\n'))
        #_______________________________________________________
#         self.tt=command.set_ModelName(self.mfile)+'.'+self._MN['SET1']['Set1'][0]
#         #print self.tt
#         self.success=OMPython.execute(command.getClassNames(self.tt))
#         self.success['SET2']['Set1']
#         fle= open('dict1.properties','w')
#         for x in range(len(self.success['SET1']['Set1'])):
#             for y in range(len(self.success['SET2']['Set1'])):
#                 self.lis.append(self.mfile+self.success['SET1']['Set1'][x]+'.'+self.success['SET2']['Set1'][y])
#                 fle.writelines(str(self.mfile+self.success['SET1']['Set1'][x]+'.'+self.success['SET2']['Set1'][y]+'\n'))
        #____________________________________________________
        self.comboBox_5.clear()
        self.comboBox_5.addItems(self.lis)
            
        #print self.lis
        
        """
        TO DO: use OMPython API to get the selected model.(Under Construction!!!)
        """
#         
        
    
    
    """function for 'output path' """
    def Output_path(self):
        self.fname = QtGui.QFileDialog.getExistingDirectory(Dialog, 'Select file')
        if self.fname:
            self.opath=str(self.fname)
            self.lineEdit_4.setText(self.opath)
        else:
            self.lineEdit_4.setText('No file selected')
             
    def Load_Resource(self):
        #self.fname = QtGui.QFileDialog.getOpenFileName(Dialog, 'Select file')
        self.sources= SimulationResources([self.fname1,'r'])
        self.sources.load_Properties()
        self.lineEdit.setText(self.sources.get_modelFile())
        #print self.sources.get_modelFile()
        self.lineEdit_2.setText(self.sources.get_libraryFile())
        #self.lineEdit_3.setText(self.sources.get_modelName())
        self.lineEdit_4.setText(self.sources.get_outputPath())
    def get_fname_save_Resource(self): 
        self.source1.set_modelFile(self.mfile)
        self.source1.set_modelName(str(self.comboBox_5.currentText()))
        self.source1.set_modelPath(self.mpath)
        self.source1.set_libraryFile(self.lfile)
        self.source1.set_libraryPath(self.lpath)
        self.source1.set_outputPath(self.opath)
        self.source1.save_Properties()  
         
    def get_save_Configuration(self):
        self.source2.set_starttime(self.lineEdit_5.text())
        self.source2.set_stoptime(self.lineEdit_6.text())
        self.source2.set_intervals(self.lineEdit_7.text())
        self.source2.set_method(str(self.comboBox.currentText()))
        self.source2.set_outputformat(str(self.comboBox_3.currentText()))
        self.source2.set_tolerance(self.lineEdit_8.text())
        self.source2.save_Properties()
        
    def get_Load_Configuration(self):
        self.OpenModelica=self.radioButton.isChecked()
        self.Dymola=self.radioButton_2.isChecked()
        self.JModelica=self.radioButton_3.isChecked()
        if self.OpenModelica==True:
            
            self.source2=SimulationConfigurationOMC([self.fname2,'r'])
            self.source2.load_Properties()
            self.lineEdit_5.setText(self.source2.get_starttime())
            self.lineEdit_6.setText(self.source2.get_stoptime())
            self.lineEdit_7.setText(self.source2.get_intervals())
            self.lineEdit_8.setText(self.source2.get_tolerance())
           
        elif self.Dymola==True:
            print "Bla Bla"
            
        elif self.JModelica==True:
            print "bla bla"
            
    """ for simulation """
    def Simulation(self):
        print sys.argv[1]
        #simCity= SimulationOMC([sys.argv[1],])
        simCity= SimulationOMC([sys.argv[1],sys.argv[2],sys.argv[3]])
        simCity.loadSources()
        results= simCity.simulate()
        h5data= simCity.saveOutputs(results)
        simCity.plotOutputs(h5data)
#         
        """ starting a new session """
# #         
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


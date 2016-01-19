'''
Created on 19 jan 2016

@author: fragom
'''

import sys, os, subprocess
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("./res/mae_modeestimation.ui")[0] # Load the UI

class ModeEstimationGUI(QtGui.QDialog, form_class):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
#         self.setWindowTitle("Mode Estimation!")
        self.btn_modeEst.clicked.connect(self.analyze_modeEstimation)
    
    def get_orderInput(self):
        return str(self.line_Order.text())
    
    def set_nameh5file(self, valor):
        self.h5simoutput= valor
    
    def set_nameh5group(self, valor):
        self.groupName= valor
        
    def set_nameh5dataset(self, valor):
        self.datasetName= valor
        
    def analyze_modeEstimation(self):
        os.chdir('C:/Users/fragom/PhD_CIM/PYTHON/SimuGUI/res/matlab')
        scriptme= []
        ''' modify the script with the data to be processed '''
        ''' h5file and dataset '''
        scriptme.append("clc; close all; clear;\n")
        scriptme.append("data= h5read('"+ str(self.h5simoutput)+ "', '"+  str(self.groupName)+ "/"+ str(self.datasetName)+"');\n")
        scriptme.append("do= data(2,:);\n")
        scriptme.append("Y= do.';\n")
        scriptme.append("order= "+ str(self.line_Order.text())+ ";\n")
        scriptme.append("[mode_freq, mode_damp]=mode_est_basic_fcn(Y, order);\n")
        scriptme.append("hdf5write('mode_estimation.h5','/mode_estimation/freq', mode_freq,'/mode_estimation/damp', mode_damp);\n")
        scriptme.append("exit\n")
        filefile = open('./run_mode_estimation.m', 'w') #os.chdir('C:/Users/fragom/PhD_CIM/PYTHON/SimuGUI/res/matlab/') before
        filefile.writelines(scriptme)
        subprocess.call("matlab -r run_mode_estimation")
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ModeEstimationGUI()
    myapp.show()
    sys.exit(app.exec_())
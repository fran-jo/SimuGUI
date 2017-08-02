'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTableWidget
from matplotlibwidget import MatplotlibWidget
from gui.mae_importdata_gui import UI_ImportData
# from matplotlib.backends.backend_qt4agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
# import matplotlib.pyplot as plt

__form_gui = uic.loadUiType("./res/mae_signalanalysis_gui.ui")[0] # Load the UI

class UI_SignalAnalysis(QtGui.QDialog, __form_gui):
    
    __simResults= None
    __measurements= None
    
    def __init__(self, parent= None, simulationResults= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.mplotSimwidget = MatplotlibWidget(self.simPlotWidget)
        self.mplotSimwidget.setGeometry(QtCore.QRect(0, 0, 400, 312))
        self.mplotSimwidget.setObjectName("mplotSimwidget")
        #
        self.mplotMeaswidget = MatplotlibWidget(self.measPlotWidget)
        self.mplotMeaswidget.setGeometry(QtCore.QRect(0, 0, 400, 312))
        self.mplotMeaswidget.setObjectName("mplotMeaswidget")
        #
    
    def __importMeasurements(self):
        windialog = UI_ImportData(self)
        windialog.setWindowTitle(self,'Import Measurements to H5 DB')
        windialog.show() 
   
    def __saveAnalysis(self):
        pass
    
'''
Created on Dec 13, 2015

@author: fran_jo, ekj05
'''

import sys, os
from PyQt4 import QtGui, uic, QtCore
from OMPython import OMCSession
from ctrl.ctrlinfogui import SimulationResources
from inout.StreamH5File import InputH5Stream
from inout.StreamCSVFile import InputCSVStream
from ctrl.validation import ValidationERA
from ctrl.analysis import QuantitativeAnalysis
from mae_modeestimation import ModeEstimationGUI
   
form_class = uic.loadUiType("./res/mae_simulation_gui.ui")[0] # Load the UI
                 
class AnalysiGUI(QtGui.QMainWindow, form_class):
    '''
    classdocs
    '''
    
    modellist=[]
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # data from simulations
        self.btn_loadSimulation.clicked.connect(self.load_simulationfile)
        self.cbx_signalSimList.activated[int].connect(self.plot_simulation)
        # data from measurements
        self.btn_loadMeasurements.clicked.connect(self.load_measurementsfile)
        self.cbx_signalMeasList.activated['QString'].connect(self.plot_measurement)
        # analysis of data
        self.btn_era.clicked.connect(self.analyze_eraMethod)
        self.btn_modeEst.clicked.connect(self.analyze_modeEstimation)
        self.btn_saveResults.clicked.connect(self.save_analysisResults)
        self.btn_rmse.clicked.connect(self.analyze_RMSE)
         
    def changeIndex(self):
        index = self.cbx_signalMeasList.currentIndex()
        if index < self.cbx_signalMeasList.count() - 1:
            self.cbx_signalMeasList.setCurrentIndex(index + 1)
        else:
            self.cbx_signalMeasList.setCurrentIndex(0)

    def load_simulationfile(self):
        #H=H5trees('./res/matlab/IEEENetworks2.IEEE_9Bus_&dymola_new_Enam.h5')
        #H=H5trees('IEEENetworks2.IEEE_9Bus_&dymola_new_Enam.h5')
        workingdir= os.getcwd()
        self.h5simoutput= QtGui.QFileDialog.getOpenFileName(self, 'Select Simulations Outputs file')
        self.h5tree= InputH5Stream([str(QtCore.QFileInfo(self.h5simoutput).absolutePath()), str(self.h5simoutput)])
        self.h5tree.open_h5()
        self.h5tree.load_h5SignalGroup()
        self.cbx_signalSimList.clear()
        self.cbx_signalSimList.addItems(self.h5tree.datasetList[:])
        os.chdir(workingdir)
        
    def plot_simulation(self, index):
        ''' plot_signal '''
        self.h5tree.del_h5signal()
        self.h5tree.load_h5SignalData(self.h5tree.datasetList[index])
        self.mplot_simOutputs.axes.plot(self.h5tree.sampleTime,self.h5tree.magnitude,
                                        self.h5tree.sampleTime,self.h5tree.angle)
        print self.h5tree.sampleTime
        self.mplot_simOutputs.axes.set_title('Variables ')
        self.mplot_simOutputs.axes.set_xlabel('Time (s)')
        self.mplot_simOutputs.axes.set_ylabel('Mgnitude')
        self.mplot_simOutputs.axes.grid()
        self.mplot_simOutputs.axes.hold(True)
        # this line force the graph to re-draw(update) 
        self.mplot_simOutputs.axes.figure.canvas.draw()
        # clean memory and allow mplot object to plot new signals
        self.mplot_simOutputs.axes.hold(False)
        
    def load_measurementsfile(self):
        workingdir= os.getcwd()
        self.csvmeasoutput= QtGui.QFileDialog.getOpenFileName(self, 'Select Measurements file')
        self.csvtree= InputCSVStream(str(self.csvmeasoutput), ',')
        self.csvtree.load_csvHeader()
        self.cbx_signalMeasList.clear()
        self.cbx_signalMeasList.addItems(self.csvtree.get_csvHeader()[1:])
        os.chdir(workingdir)
        
    def plot_measurement(self, text):
        ''' plot_signal ''' 
        self.csvtree.del_csvSignal()
        self.csvtree.load_csvSignal(str(text), 510)
        self.mplot_measurements.axes.plot(self.csvtree.sampleTime,self.csvtree.signalValues)
        print self.csvtree.sampleTime
        self.mplot_measurements.axes.set_title('PMU Data ')
        self.mplot_measurements.axes.set_xlabel('Time (s)')
        self.mplot_measurements.axes.set_ylabel('Magnitude')
        self.mplot_measurements.axes.grid()
        self.mplot_measurements.axes.hold(True)
        # this line force the graph to re-draw(update) 
        self.mplot_measurements.axes.figure.canvas.draw()
        # clean memory and allow mplot object to plot new signals
        self.mplot_measurements.axes.hold(False)
         
    ## Analysis of data 
    def analyze_eraMethod(self):
        ''' analyze_eraMethod '''
        self.lst_report.clear()
        eraEngine= ValidationERA([]) 
        eraEngine.calculate_eigenvalues(self.h5tree.magnitude)
        # analysis results to report 
        self.lst_report.addItem("Analysis of ERA Method")
        self.lst_report.addItem('A= '+ str(eraEngine.A))
        self.lst_report.addItem('B= '+ str(eraEngine.B))
        self.lst_report.addItem('C= '+ str(eraEngine.C))
        self.lst_report.addItem('Eigenvalues = '+ str(eraEngine.eigenValue))
        self.lst_report.addItem('Eigenvector = '+ str(eraEngine.eigenVector))
        # analysis results to plot  
        self.mplot_validation.axes.scatter(eraEngine.eigenValue.real,eraEngine.eigenValue.imag)
        limit_x= 1.1 # set limits for axis
        limit_y= 0.5 # set limits for axis
#         limit=np.max(np.ceil(np.absolute(eraEngine.elambda))) # set limits for axis
        self.mplot_validation.axes.set_xlim((-limit_x,limit_x))
        self.mplot_validation.axes.set_ylim((-limit_y,limit_y))
        self.mplot_validation.axes.set_title('Eigenvalues')
        self.mplot_validation.axes.set_ylabel('Imaginary')
        self.mplot_validation.axes.set_xlabel('Real')
        self.mplot_validation.axes.grid()
#         ''' this line force the graph to re-draw(update) '''
        self.mplot_validation.axes.figure.canvas.draw()

    def analyze_modeEstimation(self):
        ''' analyze_modeEstimation '''
        index= self.cbx_signalSimList.currentIndex()
        ''' open dialog for mode estimation method '''
        child_win = ModeEstimationGUI(self)
        child_win.set_nameh5file(self.h5simoutput)
        child_win.set_nameh5group(self.h5tree.cgroup.name)
        child_win.set_nameh5dataset(self.h5tree.datasetList[index])
        result = child_win.exec_()
        if result == QtGui.QDialog.Accepted:       
            ''' report results '''
            self.lst_report.clear()
            h5modest= InputH5Stream(['C:/Users/fragom/PhD_CIM/PYTHON/SimuGUI/res/matlab', 'mode_estimation.h5'])
            h5modest.open_h5()
            h5modest.load_h5Group()
#             print h5modest.datasetList
#             print h5modest.get_h5Data(h5modest.datasetList[0])
            self.lst_report.addItem('Damping: ')
            self.lst_report.addItem(str(h5modest.get_h5Data(h5modest.datasetList[0])))
            self.lst_report.addItem('Frequency: ')
            self.lst_report.addItem(str(h5modest.get_h5Data(h5modest.datasetList[1])))
            ''' TODO: plot results, two charts: damping and frequency '''
            self.mplot_validation.axes.subplot(2, 1, 1)
            self.mplot_validation.axes.plot(x1,y1,'ko-')
            self.mplot_validation.axes.set_title('Mode Estimation')
            self.mplot_validation.axes.set_ylabel('Damping')
            self.mplot_validation.axes.subplot(2, 1, 2)
            self.mplot_validation.axes.plot(x2, y2, 'r.-')
            self.mplot_validation.axes.set_ylabel('Frequency')
            self.mplot_validation.axes.set_xlabel('time(s)')
            self.mplot_validation.axes.grid()
    #         ''' this line force the graph to re-draw(update) '''
            self.mplot_validation.axes.figure.canvas.draw()
        else:
            self.lst_report.clear()
            self.lst_report.addItem('Tu! Ha petat aixo!')

    def analyze_RMSE(self):
        qa= QuantitativeAnalysis([self.h5tree.magnitude, self.csvtree.signalValues])
        # analysis results to report 
        arrayRMSE= qa.qaRMSE()
        self.lst_report.addItem("MSE= "+ str(arrayRMSE[0]))
        self.lst_report.addItem("RMSE= "+ str(arrayRMSE[1]))
        # analysis results to plot  
        signalError= qa.qaSignalError()
        self.mplot_validation.axes.plot(self.csvtree.sampleTime, signalError, 'r-')
        self.mplot_validation.axes.set_title('Error')
        self.mplot_validation.axes.set_ylabel('Time (s)')
        self.mplot_validation.axes.set_xlabel('Value')
        self.mplot_validation.axes.grid()
#         ''' this line force the graph to re-draw(update) '''
        self.mplot_validation.axes.figure.canvas.draw()
      
    def save_analysisResults(self):
        ''' TODO: save results of the era analysis '''
        # group, name of the analysis
        # file name of the network being simulated
        # dataset signal, (sampletime, real, imaginary
        # dataset eigenvalue, eigenvector 1, NxN dataset each array
        # dataset array A (NxN), B(Nx1), C(1xN), dataset each array
    
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = AnalysiGUI(None)
    myWindow.show()
    app.exec_()
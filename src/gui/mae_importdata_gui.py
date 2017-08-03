'''
Created on 19 jan 2016

@author: fragom
'''
import sys, os
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTreeWidgetItem
from inout.streamcimh5 import StreamCIMH5
from inout.streammatfile import InputMATStream
from inout.streamcsvfile import InputCSVStream
#from inout.streamoutfile import InputOUTStream
# from matplotlib.backends.backend_qt4agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
# import matplotlib.pyplot as plt

form_gui = uic.loadUiType("./res/mae_importdata_gui.ui")[0] # Load the UI

class UI_ImportData(QtGui.QDialog, form_gui):
    
    __results= None
    
    def __init__(self, parent= None, simulationResults= None, 
                 exportEnabled= True, importEnabled= True):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
    
#     def __importMAT(self, itemParent=None, branches=None):
#         ''' TODO: UI must select file '''
#         ''' .mat files resulting from Dymola or OpenModelica simulation 
#         use of ModelicaRes library'''
#         sourcemat= InputMATStream(matFile, compiler)
#         sourcemat.load_components()
#         componentsName= self.selectData(sourcemat.components, 'Select which component data to import: ')
#         sourcemat.load_variables(componentsName)
#         componentsSignals= zip(componentsName,sourcemat.variables)
#         for componentname, componentSignal in componentsSignals:
#             variablesName= self.selectData(componentSignal, 'Select which signals from components to import (per pairs): ')
#             # TODO supose user only select 2 variabler per component, what if selects more?
#             sourcemat.load_signals(componentname, variablesName)
#    
#     def __importCSV(self):
#         ''' TODO: UI must select file '''
#         sourcecsv= InputCSVStream(csvFile, delimiter)
#         sourcecsv.load_csvHeader()
# #         print sourcecsv.cheader
#         measname= self.selectData(sourcecsv.header, 'Select which component data to import: ')
#         componentname= ':'.join([measname[0].split(':')[0], measname[0].split(':')[1]])
#         sourcecsv.load_csvValues(componentname, measname[0], measname[1])
        
#     def __importOUT(self, binpath):
#         ''' TODO: UI must select psse binary path '''
#         PSSE_PATH= binpath
#         sys.path.append(PSSE_PATH)
#         os.environ['PATH']+= ';'+ PSSE_PATH
#         
#         ''' .out files resulting from psse dynamic simulations '''
#         sourceout= InputOUTStream(outfile)
#         sourceout.load_outputData()
#         selectedOutput= self.selectData(sourceout.ch_id, "Select the data to import, in pairs:")
#         sourceout.save_channelID(selectedOutput)
#         sourceout.load_channelData()
        
    def __saveSignals(self):
        ''' TODO test function '''
        ''' TODO treat multiple signals from here, using StreamCIMH5 API '''
        getSelected = self.twToImport.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            parentName= baseNode.parent().text(0)
            childName = baseNode.text(0)
        ''' TODO create paramName when the name is composed by >2 levels ex: a.b.c '''
        paramName= parentName+ '.'+ childName
        dbh5api= StreamCIMH5('./db/signals', self.__results.fbase)
        dbh5api.open(self.__results.fbase)
        if not dbh5api.exist_PowerSystemResource():
            dbh5api.add_PowerSystemResource(str(parentName))
        else:
            dbh5api.update_PowerSystemResource(str(parentName), str(parentName))
        
        if not dbh5api.exist_AnalogMeasurement():
            dbh5api.add_AnalogMeasurement(str(childName),
                                      self.__results[str(paramName)].unit, 
                                     'unitMultiplier', 
                                     'measurementType')
            dbh5api.add_AnalogValue(self.__results[str(paramName)].times().tolist(),
                                self.__results[str(paramName)].values().tolist())
        else:
            dbh5api.select_AnalogMeasurement()
            dbh5api.update_AnalogMeasurement(str(childName), self.__results[str(paramName)].unit, 
                                     'unitMultiplier', 
                                     'measurementType')
            dbh5api.update_AnalogValue(str(childName),
                                       self.__results[str(paramName)].times().tolist(),
                                       self.__results[str(paramName)].values().tolist())

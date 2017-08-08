'''
Created on 19 jan 2016

@author: fragom
'''
import platform
from PyQt4 import uic, QtCore, QtGui
from PyQt4.QtGui import QTreeWidgetItem
from inout.streamcimh5 import StreamCIMH5
from inout.streammatfile import InputMATStream
from processing import PMUData
#from inout.streamoutfile import InputOUTStream
# from matplotlib.backends.backend_qt4agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
# import matplotlib.pyplot as plt

form_gui = uic.loadUiType("./res/mae_importdata_gui.ui")[0] # Load the UI

class UI_ImportData(QtGui.QDialog, form_gui):
    
    __results= None
    __extensionFile= ''
    __selectedMeasurements= None
    
    def __init__(self, parent, simulationResults= None, 
                 exportEnabled= True, importEnabled= True):
        super(UI_ImportData, self).__init__(parent)
        self.setupUi(self)
        #
        self.btnBrowseFolder.clicked.connect(self.__browseFolder)
        self.buttonBox.accepted.connect(self.__acceptImport)
        #
        self.cbxMeasFiles.activated['QString'].connect(self.__loadByExtension)
        #
        self.btnChooseItems.clicked.connect(self.__chooseItems)
    
    def __browseFolder(self):
        carpetaName = str(QtGui.QFileDialog.getExistingDirectory(self, 'Select Folder'))
        if platform.system()== 'Windows':
            carpetaName= carpetaName.replace('\\', '/')
        splitcName= carpetaName.split('/')
        relativepath= './'+ splitcName[-2]+ '/'+ splitcName[-1]+ '/'
        self.cbxMeasFiles.clear()
        if carpetaName:
            path= QtCore.QDir(carpetaName)
            files= path.entryList(QtCore.QDir.Files, QtCore.QDir.Name)
            self.cbxMeasFiles.addItems([relativepath+ f for f in files])
        else:
            print 'Log: Please select a folder!'
            
    def __loadByExtension(self, valuefile):
        self.__extensionFile= str(valuefile).split('.')[2]
        print self.__extensionFile
        if self.__extensionFile== 'csv':
            print 'Log: Import a .csv file, PMU Measurement'
            self.__importCSV(str(valuefile))
        elif self.__extensionFile== 'out':
            print 'Log: Import a .out file, PSS/E output'
            
    def __chooseItems(self):
        self.__selectedMeasurements = QtGui.QStandardItemModel(self.lvSelectedMeasurements)
        getSelected = self.twMeasurements.selectedItems()
        for item in getSelected:
            listItem = QtGui.QStandardItem(str(item.text(0)))
            self.__selectedMeasurements.appendRow(listItem)
        self.lvSelectedMeasurements.setModel(self.__selectedMeasurements)
        
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
    def __importCSV(self, csvFile):
        self.twMeasurements.clear()
        self.__sourcecsv= PMUData(csvFile, ',')
        self.__sourcecsv.load_Measurements()
        rootItem= QTreeWidgetItem(self.twMeasurements, [csvFile])
        for value in self.__sourcecsv.measurements:
            childItem = QTreeWidgetItem()
            childItem.setText(0, value)
            rootItem.addChild(childItem)
        
    def __acceptImport(self):
        measSelection= []
        if self.__extensionFile== 'csv':
            i = 0
            while self.__selectedMeasurements.item(i):
                measSelection.append(self.__selectedMeasurements.item(i).text())
                i += 1
            #todo invoke import csv function
            self.__sourcecsv.store_Measurements(measSelection)
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
        getSelected = self.twToImport.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            parentName= baseNode.parent().text(0)
            childName = baseNode.text(0)
        ''' TODO create paramName when the name is composed by >2 levels ex: a.b.c '''
        paramName= parentName+ '.'+ childName
        dbh5api= StreamCIMH5('./db/simulation', self.__results.fbase)
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
        dbh5api.close()

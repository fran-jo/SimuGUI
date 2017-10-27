'''
Created on 19 jan 2016

@author: fragom
'''

import platform
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTreeWidgetItem
from modelicares import util
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from inout.streamcimh5 import StreamCIMH5
from modelicares import SimRes

'''TODO Import Selected variables into H5 '''

form_gui = uic.loadUiType("./res/mee_plot_gui.ui")[0] # Load the UI

class UI_Plot_MEE(QtGui.QDialog, form_gui):
    keyPressed= QtCore.pyqtSignal()
    __results= None
    __dbh5api= None
    
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
#         self.mplotwidget = MatplotlibWidget(self.centralWidget, width= 590, height= 380, dpi= 60)
#         self.mplotwidget.setGeometry(QtCore.QRect(0, 0, 590, 380))
#         self.mplotwidget.setObjectName("mplotwidget")
        self.createGraficaSimu()
        #
#         self.__results= simulationResults
#         arbol = util.tree(self.__results.names())
#         self.twVariable.clear()
#         rootItem= QTreeWidgetItem(self.twVariable, [self.__results.fbase])
#         self.__build_tree(rootItem, arbol)
#         self.twVariable.itemSelectionChanged.connect(self.__onSelectionChanged)
        #
        self.btnSaveSignals.clicked.connect(self.__saveSignals)
        self.btnBrowseMeasurements.clicked.connect(self.__browseFolder)
        self.cbxOutputs.activated['QString'].connect(self.__loadOutputFile)
        
    def createGraficaSimu(self):
        self.figureGS = Figure()
        self.canvasGS = FigureCanvas(self.figureGS)
        self.toolbarGS = NavigationToolbar(self.canvasGS, self)
        self.graficaGS = self.figureGS.add_subplot(111) 
        self.graficaGS.grid()
        # set the layout
        layoutGS = QtGui.QVBoxLayout()
        layoutGS.addWidget(self.canvasGS)
        layoutGS.addWidget(self.toolbarGS)
        layoutGS.setContentsMargins(0,0,0,0)
        self.centralWidget.setLayout(layoutGS)
        
    def keyPressEvent(self, event):
        if event.key()== QtCore.Qt.Key_Backspace:
            self.mplotwidget.clear()
    
    def __browseFolder(self):
        carpetaName = QtGui.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if platform.system()== 'Windows':
            carpetaName= carpetaName.replace('\\', '/')
        splitcName= carpetaName.split('/')
        relativepath= './'+ splitcName[-2]+ '/'+ splitcName[-1]+ '/'
        self.cbxOutputs.clear()
        if carpetaName:
            path= QtCore.QDir(carpetaName)
            files= path.entryList(QtCore.QDir.Files, QtCore.QDir.Name)
            self.cbxOutputs.addItems([relativepath+ f for f in files])
        else:
            print 'Log: Please select a folder!'
        self.cbxOutputs.setFocus()
            
    def __loadOutputFile(self, valuefile):
        self.__results = SimRes(str(valuefile))
        arbol = util.tree(self.__results.names())
        self.twVariable.clear()
        rootItem= QTreeWidgetItem(self.twVariable, [self.__results.fbase])
        self.__build_tree(rootItem, arbol)
        self.twVariable.itemSelectionChanged.connect(self.__onSelectionChanged)
    
    # This function has been copied and modified from ModelicaRes version 0.12
    # (Kevin Davies,
    # http://kdavies4.github.io/ModelicaRes/,
    # BSD License).
    def __build_tree(self, itemParent=None, branches=None):
        #itemParent.setExpanded(True)
        if type(branches) is dict:
            for key, val in sorted(branches.iteritems()):
                childItem = QTreeWidgetItem()
                childItem.setText(0, unicode(key))
                itemParent.addChild(childItem)
                if type(val) is dict:
                    self.__build_tree(childItem, val)
        else:
            childItem = QTreeWidgetItem()
            childItem.setText(0, unicode(branches))
            itemParent.addChild(childItem)
   
    def selectionChanged(self):
        ''' TODO: it has to be a better way to get a full name from the tree view.
        By full name I mean 1stlevel.2ndlevel.3rdlevel.etc....'''
        getSelected = self.twVariable.selectedItems()
        selectedParams= []
        for baseNode in getSelected:
            #baseNode = getSelected[0]
            parentName= str(baseNode.parent().text(0))
            childName= baseNode.text(0)
            if baseNode.parent().parent()!= None:
                grandpaName= str(baseNode.parent().parent().text(0))
            if grandpaName== self.__results.fbase:
                selectedParams.append(parentName+ '.'+ childName)
            else:
                selectedParams.append(grandpaName+ '.'+ parentName+ '.'+ childName)
        return selectedParams
        
    def __onSelectionChanged(self):
        
        try:
            self.graficaGS.clear()
            selectedParams= self.selectionChanged()
            if selectedParams== []:
                self.canvasGS.clear()
            else:
                self.__view_Signal(selectedParams, self.__results)
        except UnboundLocalError:
            self.graficaGS.clear()
        
    # This function has been copied and modified from ModelicaRes version 0.12
    # (Kevin Davies,
    # http://kdavies4.github.io/ModelicaRes/,
    # BSD License)
    def __view_Signal(self, signalsToPlot, sim, event= None):
        '''Show the variable's attributes and a small plot.
        fix it using the matplotlibwidget
        Using ModelicaRes for ploting simulation signals'''
        for name in signalsToPlot:
            name= str(name)
            text = 'Name: ' + name
            text += '\n' + 'Description: ' + sim[name].description
            text += '\n' + 'unit: ' + sim[name].unit
            text += '\n' + 'displayUnit: ' + sim[name].displayUnit
            self.graficaGS.plot(sim[name].times().tolist(), sim[name].values().tolist())
            self.graficaGS.set_title("Signal", fontsize=14)
            self.graficaGS.set_xlabel("Time (s)", fontsize=12)
            self.graficaGS.set_ylabel(sim[name].displayUnit, fontsize=12)
            #TODO Add legend automatically, bottom-right corner
            self.graficaGS.hold(True)
            self.canvasGS.draw()  
            
    def __saveSignals(self):
        ''' TODO treat multiple signals from here, using StreamCIMH5 API '''
        selectedParams= self.selectionChanged()
        dbh5api= StreamCIMH5('./db/simulation', self.__results.fbase)
        dbh5api.open(self.__results.fbase, mode= 'a')
        for paramName in selectedParams:
            parentName= paramName.split('.')[-2]
            childName= paramName.split('.')[-1]
            if not dbh5api.exist_PowerSystemResource(str(parentName)):
                dbh5api.add_PowerSystemResource(str(parentName))
            else:
                dbh5api.update_PowerSystemResource(str(parentName), str(parentName))
            
            if not dbh5api.exist_AnalogMeasurement(str(childName)):
                dbh5api.add_AnalogMeasurement(str(childName),
                                          self.__results[str(paramName)].unit, 
                                         'unitMultiplier')
                dbh5api.add_AnalogValue(self.__results[str(paramName)].times().tolist(),
                                    self.__results[str(paramName)].values().tolist())
            else:
                dbh5api.select_AnalogMeasurement()
                dbh5api.update_AnalogMeasurement(str(childName), self.__results[str(paramName)].unit, 
                                         'unitMultiplier')
                dbh5api.update_AnalogValue(str(childName),
                                           self.__results[str(paramName)].times().tolist(),
                                           self.__results[str(paramName)].values().tolist())
        dbh5api.close()
        #TODO log export variables, success or failure
        
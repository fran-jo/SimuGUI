'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTreeWidgetItem
from modelicares import util
from matplotlibwidget import MatplotlibWidget
from inout.streamcimh5 import StreamCIMH5
# from matplotlib.backends.backend_qt4agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
# import matplotlib.pyplot as plt

form_gui = uic.loadUiType("./res/mee_plot_gui.ui")[0] # Load the UI

class UI_Plot_MEE(QtGui.QDialog, form_gui):
    
    __results= None
    __dbh5api= None
    
    def __init__(self, parent= None, simulationResults= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.mplotwidget = MatplotlibWidget(self.centralWidget)
        self.mplotwidget.setGeometry(QtCore.QRect(0, 0, 520, 380))
        self.mplotwidget.setObjectName("mplotwidget")
        #
        self.__results= simulationResults
        arbol = util.tree(self.__results.names())
        self.twVariable.clear()
        rootItem= QTreeWidgetItem(self.twVariable, [self.__results.fbase])
        self.__build_tree(rootItem, arbol)
        self.twVariable.itemSelectionChanged.connect(self.__onSelectionChanged)
        #
        self.btnSaveSignals.clicked.connect(self.__saveSignals)
        #
        self.btnLoadSignals.clicked.connect(self.__loadSignals)
   
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
   
    def __onSelectionChanged(self):
        """Update the variable's attributes and plot.
        """
        getSelected = self.twVariable.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            parentName= str(baseNode.parent().text(0))
            childName= baseNode.text(0)
            if baseNode.parent().parent()!= None:
                grandpaName= str(baseNode.parent().parent().text(0))
            if grandpaName== self.__results.fbase:
                paramName= parentName+ '.'+ childName
            else:
                paramName= grandpaName+ '.'+ parentName+ '.'+ childName
        self.__view_Signal(str(paramName), self.__results)
        
    # This function has been copied and modified from ModelicaRes version 0.12
    # (Kevin Davies,
    # http://kdavies4.github.io/ModelicaRes/,
    # BSD License)
    def __view_Signal(self, name, sim):
        '''Show the variable's attributes and a small plot.
        fix it using the matplotlibwidget
        Using ModelicaRes for ploting simulation signals'''
        if name:
            text = 'Name: ' + name
            text += '\n' + 'Description: ' + sim[name].description
            text += '\n' + 'unit: ' + sim[name].unit
            text += '\n' + 'displayUnit: ' + sim[name].displayUnit
            ''' TODO updated title, xAxis and yAxis labels
            TODO handle multiple signals- hold option
            TODO plot GUI to accept HDF5 format
            TODO export to CSV '''
            self.mplotwidget.theplot.set_title('Something here')
            self.mplotwidget.theplot.set_xlabel('Time (s)')
            self.mplotwidget.theplot.set_ylabel(sim[name].description)
            self.mplotwidget.plot(sim[name].times().tolist(), sim[name].values().tolist())
            # this line force the graph to re-draw(update) 
            #self.mplotwidget.draw()
#             self.mplotOuts.axes.set_ylabel(name + " / $%s$" %
#                                  str(sim[name].unit))
#            self.mplotOuts.axes.set_xlabel("Time / s")
        else:
            print "nothing to plot"
            
    def __saveSignals(self):
        ''' TODO treat multiple signals from here, using StreamCIMH5 API '''
        getSelected = self.twVariable.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            parentName= str(baseNode.parent().text(0))
            childName= baseNode.text(0)
            if baseNode.parent().parent()!= None:
                grandpaName= str(baseNode.parent().parent().text(0))
            if grandpaName== self.__results.fbase:
                paramName= parentName+ '.'+ childName
            else:
                paramName= grandpaName+ '.'+ parentName+ '.'+ childName
        dbh5api= StreamCIMH5('./db/h5', self.__results.fbase)
        dbh5api.open(self.__results.fbase, mode= 'a')
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
        
        
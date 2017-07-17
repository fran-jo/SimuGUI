'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic
from PyQt4.QtGui import QTreeWidgetItem
from modelicares import util
from matplotlibwidget import MatplotlibWidget
# from matplotlib.backends.backend_qt4agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
# import matplotlib.pyplot as plt

form_gui = uic.loadUiType("./res/msv_plot_gui.ui")[0] # Load the UI

class UI_Plot(QtGui.QDialog, form_gui):
    
    __results= None
    
    def __init__(self, parent= None, simulationResults= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.mplotwidget = MatplotlibWidget(self.centralWidget)
        #
        self.__results= simulationResults
        arbol = util.tree(self.__results.names())
#         print self.__results.names()
#         print self.__results['Line10_11.P21']
        self.twVariable.clear()
        rootItem= QTreeWidgetItem(self.twVariable, [self.__results.fbase])
        self.__build_tree(rootItem, arbol)
        self.twVariable.itemSelectionChanged.connect(self.__onSelectionChanged)
    
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
            parentName= baseNode.parent().text(0)
            childName = baseNode.text(0)
        #print "hijoeputa ", childName
        ''' TODO create paramName when the name is composed by >2 levels ex: a.b.c '''
        paramName= parentName+ '.'+ childName
        self.__preview(str(paramName), self.__results) #TODO
        
    def __preview(self, name, sim):
        """Show the variable's attributes and a small plot.
        fix it using the matplotlibwidget"""
        if name:
            text = 'Name: ' + name
            text += '\n' + 'Description: ' + sim[name].description
            text += '\n' + 'unit: ' + sim[name].unit
            text += '\n' + 'displayUnit: ' + sim[name].displayUnit
            print text
            print sim[name].times().__class__
            print sim[name].values().__class__
            print sim[name].times()
            print sim[name].values()
            self.mplotwidget.axes.plot(sim[name].times(), sim[name].values())
            self.mplotwidget.axes.set_title('Something here')
            self.mplotwidget.axes.set_xlabel('Time (s)')
            self.mplotwidget.axes.set_ylabel('Value')
            self.mplotwidget.axes.grid()
            # this line force the graph to re-draw(update) 
            self.mplotwidget.draw()
#             self.mplotOuts.axes.set_ylabel(name + " / $%s$" %
#                                  str(sim[name].unit))
#            self.mplotOuts.axes.set_xlabel("Time / s")
        else:
            print "nothing to plot"
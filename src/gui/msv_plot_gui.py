'''
Created on 19 jan 2016

@author: fragom
'''

from PyQt4 import QtGui, uic
from PyQt4.QtGui import QTreeWidgetItem
from six import string_types
from collections import OrderedDict
from modelicares import util

form_gui = uic.loadUiType("./res/msv_plot_gui.ui")[0] # Load the UI

class UI_Plot(QtGui.QDialog, form_gui):
    
    __results= None
    
    def __init__(self, parent= None, simulationResults= None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        #
        self.__results= simulationResults
        
        arbol = util.tree(self.__results.names, self.__results.names, container=OrderedDict)
        self.__build_tree(arbol, QTreeWidgetItem(self.twVariable, self.__results.fbase))
    
    def __build_tree(self, branches=None, itemParent=None):
        for key in branches.keys():
            if isinstance(branches[key], string_types):
                QTreeWidgetItem(itemParent, branches[key])
            else:
                newItem= QTreeWidgetItem(itemParent,'')
                self.__build_tree(branches[key], newItem)  # Recursion
    
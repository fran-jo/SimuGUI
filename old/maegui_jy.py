'''
Created on 17 jun 2015

@author: fragom
'''
from java.awt import BorderLayout, Dimension, GridLayout, GridBagLayout, GridBagConstraints
from javax.swing import JFrame, JPanel, JScrollPane, JComboBox,\
    JButton, JTree, JTextArea
from javax.swing.tree import DefaultMutableTreeNode
from javax.swing import SwingUtilities
from javax.swing import JFileChooser, WindowConstants
from java.io import File
from javax.swing.filechooser import FileNameExtensionFilter
from java.beans import PropertyChangeListener
from java.lang import Runnable
# from src.classes import PhasorMeasH5
# from src.data import signal

class SimoutPanel(JPanel, PropertyChangeListener): 
    
    def loadSimOut(self, event):
        chooseFile = JFileChooser()
        filtro = FileNameExtensionFilter("Output files (.h5)", ['h5'])
        chooseFile.addChoosableFileFilter(filtro)
        ret = chooseFile.showDialog(self.frame, "Choose simulation result")
        if ret == JFileChooser.APPROVE_OPTION:
            faile= chooseFile.getSelectedFile()
            self.cbfilesimOut.addItem(faile.getPath())
            self.cbfilesimOut.selectedItem(faile.getPath())

        h5pmu= PhasorMeasH5.PhasorMeasH5(faile)
        h5pmu.open_h5()
        h5pmu.load_h5('pwLine4', 'V')
        # result: 2 vectors per variable, work with pwLine4.n.vr, pwLine4.n.vi
        senyal= h5pmu.get_senyal()
        print senyal
         
    def __init__(self):
        # Panel for Simulation outputs
        self.setLayout(BorderLayout())
        # PAGE_START
        ''' show group/dataset names in the list (component/variable) names '''
        p1= JPanel()
        p1.setLayout(GridLayout(1,2))
        self.cbfilesimOut = JComboBox([])
        bfilesimOut= JButton('Sim Output', actionPerformed= self.loadSimOut)
        p1.add(self.cbfilesimOut)
        p1.add(bfilesimOut)
        self.add(p1, BorderLayout.PAGE_START)
        # LINE_START
        root = DefaultMutableTreeNode('VarOutputs')
        self.tree = JTree(root)
        scrollPane = JScrollPane()  # add a scrollbar to the viewport
        scrollPane.setPreferredSize(Dimension(230,320))
        scrollPane.getViewport().setView((self.tree))
        p2 = JPanel()
        p2.add(scrollPane)
        self.add(p2, BorderLayout.LINE_START)
        # CENTER
        ''' represent a signal with matplot lib in textarea places '''
        graficSim= JTextArea()
        self.add(graficSim, BorderLayout.CENTER)

class MeasPanel(JPanel, PropertyChangeListener):  
    
    def loadMeasOut(self,event):
    
        pass
        
    def __init__(self):
        # Panel for Measurements
        self.setLayout(BorderLayout())
        # PAGE_START
        ''' show group/dataset names in the list (component/variable) names '''
        self.cbfilemeasOut = JComboBox([])
        bfilemeasOut= JButton('Measurements', actionPerformed= self.loadMeasOut)
        p3= JPanel()
        p3.setLayout(GridLayout(1,2))
        p3.add(self.cbfilemeasOut)
        p3.add(bfilemeasOut)
        self.add(p3, BorderLayout.PAGE_START)
        # LINE_START
        root = DefaultMutableTreeNode('VarMeasurements')
        self.tree = JTree(root)
        scrollPane = JScrollPane()  # add a scrollbar to the viewport
        scrollPane.setPreferredSize(Dimension(230,320))
        scrollPane.getViewport().setView((self.tree))
        p4 = JPanel()
        p4.add(scrollPane)
        self.add(p4, BorderLayout.LINE_START)
        # CENTER
        ''' represent a signal with matplot lib in textarea places '''
        graficMeas= JTextArea()
        self.add(graficMeas, BorderLayout.CENTER)
    
class ReportPanel(JPanel, PropertyChangeListener):
      
    def modeComputation(self, event):
        ''' invoke matlab method for mode estimation '''
        pass 
    
    def __init__(self):
        # Panel for Measurements
        self.setLayout(BorderLayout())
        # LINE_START
        p3= JPanel()
        p3.setLayout(GridLayout(3,1))
        button1= JButton('Mode Estimation', actionPerformed= self.modeComputation)
        button2= JButton('button2', actionPerformed= self.modeComputation)
        button3= JButton('button3', actionPerformed= self.modeComputation)
        p3.add(button1)
        p3.add(button2)
        p3.add(button3)
        self.add(p3, BorderLayout.LINE_START)
        # LINE_END
        reportMeas= JPanel()
        reportMeas.setSize(Dimension(800,640))
        self.add(reportMeas, BorderLayout.CENTER)
        
###########################################################################        
def createAndShowGUI():
    # Create the GUI and show it. As with all GUI code, this must run
    # on the event-dispatching thread.
    frame = JFrame("MAE ")
    frame.setSize(1024, 768)
    panel= JPanel()
    panel.setLayout(GridBagLayout())
    
    #Create and set up the content pane.
    psimures= SimoutPanel()
    psimures.setOpaque(True)
    c = GridBagConstraints()
    c.fill = GridBagConstraints.HORIZONTAL
    c.weightx = 1
    c.gridx = 0
    c.gridy = 0
    panel.add(psimures, c);
    pmeasure= MeasPanel()
    pmeasure.setOpaque(True)
    c = GridBagConstraints()
    c.fill = GridBagConstraints.HORIZONTAL
    c.weightx = 1
    c.gridx = 0
    c.gridy = 1
    panel.add(pmeasure, c);
    preport = ReportPanel()
    preport.setOpaque(True)
    c = GridBagConstraints()
    c.fill = GridBagConstraints.VERTICAL
    c.weighty = 1
    c.gridx = 1
    c.gridy = 0
    c.gridheight= 2
    panel.add(preport,c)
    # show the GUI
    
    frame.add(panel)
#     frame.add(pmeasure)
#     frame.add(preport)
    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    frame.setVisible(True)
 
###########################################################################
class Runnable(Runnable):
    def __init__(self, runFunction):
        self._runFunction = runFunction


    def run(self):
        self._runFunction()

###########################################################################         
if __name__ == '__main__':
    SwingUtilities.invokeLater(Runnable(createAndShowGUI))
    ''' load the current configuration from resources.properties and 
    configuration.properties '''
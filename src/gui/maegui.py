'''
Created on 17 jun 2015

@author: fragom
'''
from java.awt import BorderLayout, Dimension, GridLayout
from javax.swing import JSplitPane, JFrame, JPanel, JScrollPane, JComboBox,\
    JButton, JTree, JTextArea
from javax.swing.tree import DefaultMutableTreeNode
from javax.swing import JFileChooser, WindowConstants
from java.io import File
from javax.swing.filechooser import FileNameExtensionFilter
            
class MainGUI:
    '''
    classdocs
    '''
    def loadSimOut(self, event):
        chooseFile = JFileChooser()
        chooseFile.setCurrentDirectory(File('C:\Users\fragom\PhD_CIM\Modelica\Models')) 
        filtro = FileNameExtensionFilter("Output files (.csv .h5 .mat)", ['csv','h5','mat'])
        chooseFile.addChoosableFileFilter(filtro)
        ret = chooseFile.showDialog(self.frame, "Choose simulation result")
        if ret == JFileChooser.APPROVE_OPTION:
            faile= chooseFile.getSelectedFile()
            self.cbfilesimOut.addItem(faile.getPath())
            self.cbfilesimOut.selectedItem(faile.getPath())
        print faile
        
    def loadMeasOut(self,event):
        chooseFile = JFileChooser()
        chooseFile.setCurrentDirectory(File('C:\Users\fragom\PhD_CIM\Modelica\Models')) 
        filtro = FileNameExtensionFilter("Measurements files (.csv .h5 .mat)", ['csv','h5','mat'])
        chooseFile.addChoosableFileFilter(filtro)
        ret = chooseFile.showDialog(self.frame, "Choose Measurements result")
        if ret == JFileChooser.APPROVE_OPTION:
            faile= chooseFile.getSelectedFile()
            self.cbfilemeasOut.addItem(faile.getPath())
            self.cbfilemeasOut.selectedItem(faile.getPath())
        print faile
    
    def __init__(self):
        self.frame = JFrame("MAE ")
        self.frame.setSize(1024, 768)
        self.frame.setLayout(BorderLayout())
        splitPane = JSplitPane(JSplitPane.VERTICAL_SPLIT)
        splitPane.setDividerLocation(382)
        # Panel for Simulation outputs
        psimOut= JPanel()
        psimOut.setLayout(BorderLayout())
        psimOut.setPreferredSize(Dimension(1024,384))
        psimOut.setSize(Dimension(1024,384))
        # PAGE_START
        p1= JPanel()
        p1.setLayout(GridLayout(1,2))
        self.cbfilesimOut = JComboBox([])
        bfilesimOut= JButton('Sim Output', actionPerformed= self.loadSimOut)
        p1.add(self.cbfilesimOut)
        p1.add(bfilesimOut)
        psimOut.add(p1, BorderLayout.PAGE_START)
        # LINE_START
        root = DefaultMutableTreeNode('VarOutputs')
        self.tree = JTree(root)
        scrollPane = JScrollPane()  # add a scrollbar to the viewport
        scrollPane.setPreferredSize(Dimension(230,320))
        scrollPane.getViewport().setView((self.tree))
        p2 = JPanel()
        p2.add(scrollPane)
        psimOut.add(p2, BorderLayout.LINE_START)
        # CENTER
        graficSim= JTextArea()
        psimOut.add(graficSim, BorderLayout.CENTER)
  
        # Panel for Measurements
        pmeasOut= JPanel()
        pmeasOut.setLayout(BorderLayout())
        pmeasOut.setPreferredSize(Dimension(1024,384))
        # PAGE_START
        self.cbfilemeasOut = JComboBox([])
        bfilemeasOut= JButton('Measurements', actionPerformed= self.loadMeasOut)
        p3= JPanel()
        p3.setLayout(GridLayout(1,2))
        p3.add(self.cbfilemeasOut)
        p3.add(bfilemeasOut)
        pmeasOut.add(p3, BorderLayout.PAGE_START)
        # LINE_START
        root = DefaultMutableTreeNode('VarMeasurements')
        self.tree = JTree(root)
        scrollPane = JScrollPane()  # add a scrollbar to the viewport
        scrollPane.setPreferredSize(Dimension(230,320))
        scrollPane.getViewport().setView((self.tree))
        p4 = JPanel()
        p4.add(scrollPane)
        pmeasOut.add(p4, BorderLayout.LINE_START)
        # CENTER
        graficMeas= JTextArea()
        pmeasOut.add(graficMeas, BorderLayout.CENTER)
        
        # show the GUI
        splitPane.add(psimOut)
        splitPane.add(pmeasOut);
        self.frame.add(splitPane)
        self.frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        self.frame.setVisible(True)
    
if __name__ == '__main__':
    MainGUI()
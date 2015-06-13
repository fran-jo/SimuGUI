'''
Created on 10 jun 2015

@author: fragom
'''
from javax.swing import JPanel, JMenu, JMenuItem, JMenuBar, JFrame, JTree,\
    JTextArea, JButton, JComboBox
from javax.swing import JSplitPane, JTabbedPane, JLabel, JScrollPane
from javax.swing import JFileChooser, WindowConstants
from javax.swing.filechooser import FileNameExtensionFilter
from java.awt import BorderLayout, Dimension, GridLayout
from java.io import File
from ctrl.ctrlproperties import CtrlProperties
from ctrl.commandOMC import CommandOMC
import OMPython
import os

class MainGUI:
    '''
    classdocs
    '''
    def onOpenFile(self, event):
        ''' remember to change'''
        chooseFile = JFileChooser()
        chooseFile.setCurrentDirectory(File('C:\Users\fragom\PhD_CIM\Modelica\Models')) 
        filtro = FileNameExtensionFilter("mo files", ["mo"])
        chooseFile.addChoosableFileFilter(filtro)
        ret = chooseFile.showDialog(self.panel, "Choose file")
        if ret == JFileChooser.APPROVE_OPTION:
            self.faile= chooseFile.getSelectedFile()
            if event.getActionCommand() == "Load Model":
                self.cbMoFile.addItem(self.faile.getPath())
                self.cbMoFile.selectedItem= self.faile.getPath()
            if event.getActionCommand() == "Load Library":
                self.cbMoLib.addItem(self.faile.getPath())
                self.cbMoLib.selectedItem= self.faile.getPath()
            print self.faile
    
    def onOpenModel(self, event):
        omc= CommandOMC()
        sesion= OMPython.OMCSession()
        comando= omc.loadFile(self.cbMoFile.selectedItem)
        sesion.execute(comando)
        comando= omc.getClassNames('SmarTSLab.Networks')
        success= sesion.execute(comando)
        print success
        self.cb3.SetModel(self.dModel)
        
    def onOpenFolder(self, event):
        chooseFile = JFileChooser()
        chooseFile.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        ret = chooseFile.showDialog(self.panel, "Choose folder")
        if ret == JFileChooser.APPROVE_OPTION:
            self.faile= chooseFile.getSelectedFile()
            self.cbOutDir.addItem(self.faile.getPath())
            self.cbOutDir.selectedItem= self.faile.getPath()
            
    def simulateMe(self, event):
        self.comandArea.setText("Simulate Me")
    
    def saveConfigOMC(self,event):
        config= CtrlProperties('./res/simConfiguration.properties')
        config.setmodelPath(self.cbMoFile.selectedItem)
        config.setmodelFile(self.cbMoFile.selectedItem)
        '''TODO Open .mo file, when loaded, and get model names '''
        config.setmodelName('self.cb3.selectedItem')
        config.setlibraryPath(self.cbMoLib.selectedItem)
        config.setlibraryFile(self.cbMoLib.selectedItem)
        config.setoutputPath(self.cbOutDir.selectedItem)
        config.saveProperties('/Users/fran_jo/PhD_CIM/PYTHON/ScriptMEE/config/simParametersOMC.properties', \
                              'Simulation parameters for OMC')
    
    def cbSelect(self,event):
        selected = self.cb1.selectedIndex
        if selected >= 0:
            data = self.data[selected]
            self.label.text = data + " selected"
  
    def __init__(self):
        self.open= False
        self.panel = JPanel()
        self.panel.setLayout(BorderLayout())
        frame = JFrame("GUI Development ")
        frame.setSize(800, 600)
        frame.setLayout(BorderLayout())
        splitPane = JSplitPane(JSplitPane.VERTICAL_SPLIT);
        
        # Create the menu
        '''Menu File'''
        jMenuBar1 = JMenuBar()
        jMenu1 = JMenu()
        jMenu1.setText('File')
        jMenuItem1 = JMenuItem('Open', actionPerformed= self.onOpenFile)
        jMenuItem2 = JMenuItem()
        jMenuItem2.setText('Exit')
        jMenu1.add(jMenuItem1)
        jMenu1.add(jMenuItem2)
        '''Menu Simulation'''
        jMenu2 = JMenu()
        jMenu2.setText('Simulation')
        jMenuItem21 = JMenuItem('Simulation Options')
        jMenuItem23 = JMenuItem('Generate FMU')
        jMenu2.add(jMenuItem21)
        jMenu2.add(jMenuItem23)
        '''Add menu to menu bar and frame'''
        jMenuBar1.add(jMenu1)
        jMenuBar1.add(jMenu2)
        frame.setJMenuBar(jMenuBar1)
        
        # Create main tab panel
        ''' OpenModelica Panel '''
        psimures= JPanel()
        psimures.setLayout(GridLayout(5,2))
        psimures.setPreferredSize(Dimension(800,400))
        simBoton1= JButton('Load Model',actionPerformed=self.onOpenFile)
        self.dModelFile = []
        self.cbMoFile = JComboBox(self.dModelFile)
        simBoton2= JButton('Load Library',actionPerformed=self.onOpenFile)
        self.dLibFile = []
        self.cbMoLib = JComboBox(self.dLibFile)
        simBoton3= JButton('Select Model',actionPerformed=self.onOpenModel)
        self.dModel = []
        self.cb3 = JComboBox(self.dModel)
        simBoton4= JButton('Output Path',actionPerformed=self.onOpenFolder)
        self.dOutPath = []
        self.cbOutDir = JComboBox(self.dOutPath)
        simBoton5= JButton('Simulate',actionPerformed=self.simulateMe)
        simBoton6= JButton('Save Config',actionPerformed=self.saveConfigOMC)
        ''' adding components to the gui '''
        psimures.add(self.cbMoFile)
        psimures.add(simBoton1)
        psimures.add(self.cbMoLib)
        psimures.add(simBoton2)
        psimures.add(self.cb3)
        psimures.add(simBoton3)
        psimures.add(self.cbOutDir)
        psimures.add(simBoton4)
        psimures.add(simBoton5)
        psimures.add(simBoton6)
        
        ''' panel model '''
        simTabPane = JTabbedPane(JTabbedPane.BOTTOM)
        pOMC = JPanel()
        pOMC.setLayout(BorderLayout())
        ''' OpenModelica Panel '''
#         pscroll= JScrollPane()
#         arbol= JTree()
#         arbol.setPreferredSize(Dimension(200,500))
        self.label = JLabel('self.faile.name')
        pOMC.add(self.label,BorderLayout.PAGE_START)
#         pOMC.add(pscroll.add(arbol),BorderLayout.LINE_START)
        simTabPane.addTab("OpenModelica", pOMC)
        ''' JModelica Panel '''
        pJM = JPanel(BorderLayout())
        areatext= JTextArea()
        areatext.alignmentX = pJM.CENTER_ALIGNMENT
        pJM.add(areatext, BorderLayout.CENTER)
        simTabPane.addTab("JModelica", pJM)
        ''' Dymola Panel '''
        pDY = JPanel(BorderLayout())
        areatext= JTextArea()
        areatext.alignmentX = pDY.CENTER_ALIGNMENT
        pDY.add(areatext, BorderLayout.CENTER)
        simTabPane.addTab("Dymola", pDY)
        
        # show the GUI
        splitPane.add(psimures)
        splitPane.add(simTabPane);
        frame.add(splitPane)
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        frame.setVisible(True)
            
if __name__ == '__main__':
    MainGUI()
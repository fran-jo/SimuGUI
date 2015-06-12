'''
Created on 10 jun 2015

@author: fragom
'''
from javax.swing import JPanel, JMenu, JMenuItem, JMenuBar, JFrame, JTree,\
    JTextArea, JButton, JTextField, JComboBox
from javax.swing import JSplitPane, JTabbedPane, JLabel, JScrollPane
from javax.swing import JFileChooser, WindowConstants
from javax.swing.filechooser import FileNameExtensionFilter
from java.awt import BorderLayout, Dimension, GridLayout, FlowLayout
from ctrl.ctrlproperties import CtrlProperties

class MainGUI:
    '''
    classdocs
    '''
    def onOpenFile(self, event):
        chooseFile = JFileChooser()
        filtro = FileNameExtensionFilter("mo files", ["mo"])
        chooseFile.addChoosableFileFilter(filtro)
        ret = chooseFile.showDialog(self.panel, "Choose file")
        if ret == JFileChooser.APPROVE_OPTION:
            self.faile= chooseFile.getSelectedFile()
#             sender= event.getSource()
            if event.getActionCommand() == "Load Model":
                self.cb1.addItem(self.faile.name)
                self.cb1.selectedItem= self.faile.name
            if event.getActionCommand() == "Load Library":
                self.cb2.addItem(self.faile.name)
                self.cb2.selectedItem= self.faile.name
            print self.faile
    
    def onOpenModel(self, event):
        print "modelo"
        
    def onOpenFolder(self, event):
        chooseFile = JFileChooser()
        filtro = FileNameExtensionFilter("mo files", ["mo"])
        chooseFile.addChoosableFileFilter(filtro)
        ret = chooseFile.showDialog(self.panel, "Choose file")
        if ret == JFileChooser.APPROVE_OPTION:
            self.faile= chooseFile.getSelectedFile()
#             sender= event.getSource()
            if event.getActionCommand() == "Output Path":
                self.cb4.addItem(self.faile.name)
                self.cb4.selectedItem= self.faile.name
            print self.faile
            
    def simulateMe(self, event):
        self.comandArea.setText("Simulate Me")
    
    def saveConfig(self,event):
        '''TODO: save the data from text boxes to corresponding .properties file '''
        config= CtrlProperties('./res/simConfiguration.properties')
        config.setmodelPath(self.cb1.selectedItem)
        config.setmodelFile(self.faile.name)
        config.setmodelName(self.cb3.selectedItem)
        config.setlibraryPath(self.cb2.selectedItem)
        config.setlibraryFile(self.cb2.selectedItem)
        config.setoutputPath(self.cb4.selectedItem)
        config.saveProperties()
    
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
        compilerTabPane= JTabbedPane(JTabbedPane.TOP)
        compilerTabPane.setPreferredSize(Dimension(800,400))
        ''' OpenModelica Panel '''
        pOMC= JPanel()
        pOMC.setLayout(GridLayout(5,2))
        simBoton1= JButton('Load Model',actionPerformed=self.onOpenFile)
        self.dModelFile = []
        self.cb1 = JComboBox(self.dModelFile)
        simBoton2= JButton('Load Library',actionPerformed=self.onOpenFile)
        self.dLibFile = []
        self.cb2 = JComboBox(self.dLibFile)
        simBoton3= JButton('Select Model',actionPerformed=self.onOpenModel)
        self.dModel = []
        self.cb3 = JComboBox(self.dModel)
        simBoton4= JButton('Output Path',actionPerformed=self.onOpenFolder)
        self.dOutPath = []
        self.cb4 = JComboBox(self.dOutPath)
        simBoton5= JButton('Simulate',actionPerformed=self.simulateMe)
        simBoton6= JButton('Save Config',actionPerformed=self.saveConfig)
        ''' adding components to the gui '''
        pOMC.add(self.cb1)
        pOMC.add(simBoton1)
        pOMC.add(self.cb2)
        pOMC.add(simBoton2)
        pOMC.add(self.cb3)
        pOMC.add(simBoton3)
        pOMC.add(self.cb4)
        pOMC.add(simBoton4)
        pOMC.add(simBoton5)
        pOMC.add(simBoton6)
        ''' JModelica Panel '''
        pJM= JPanel()
        pJM.setLayout(BorderLayout())
        ''' Dymola Panel '''
        pDY= JPanel()
        pDY.setLayout(BorderLayout())
        compilerTabPane.addTab("Dymola", pDY)
        compilerTabPane.addTab("JModelica", pJM)
        compilerTabPane.addTab("OpenModelica", pOMC)
        
#         self.comandArea= JTextField('Type something here',50)
#         simBoton= JButton('Simulate Me',actionPerformed=self.simulateMe)
#         headerPanel.add(self.comandArea)
#         headerPanel.add(simBoton)
        
        ''' panel model '''
        simTabPane = JTabbedPane(JTabbedPane.BOTTOM)
        pModel = JPanel()
        pModel.setLayout(BorderLayout())
        pscroll= JScrollPane()
        ''' inside panel model '''
        arbol= JTree()
        arbol.setPreferredSize(Dimension(200,500))
        self.label = JLabel('self.faile.name')
        pModel.add(self.label,BorderLayout.PAGE_START)
        pModel.add(pscroll.add(arbol),BorderLayout.LINE_START)
        simTabPane.addTab("Model View", pModel)
        ''' panel results '''
        panelRes = JPanel(BorderLayout())
        areatext= JTextArea()
        areatext.alignmentX = panelRes.CENTER_ALIGNMENT
        panelRes.add(areatext, BorderLayout.CENTER)
        simTabPane.addTab("Results View", panelRes)
        
        # show the GUI
        splitPane.add(compilerTabPane)
        splitPane.add(simTabPane);
        frame.add(splitPane)
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        frame.setVisible(True)
            
if __name__ == '__main__':
    MainGUI()
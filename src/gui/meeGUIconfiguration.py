'''
Created on 10 jun 2015

@author: fragom
'''
from javax.swing import JPanel, JMenu, JMenuItem, JMenuBar, JFrame,\
    JButton, JComboBox, JTextField
from javax.swing import JSplitPane, JRadioButton, JLabel
from javax.swing import JFileChooser, WindowConstants
from javax.swing.filechooser import FileNameExtensionFilter
from java.awt import BorderLayout, Dimension, GridLayout
from java.io import File
from ctrl.ctrlproperties import CtrlProperties, PropertiesConfigJM, PropertiesConfigOMCDY
from ctrl.commandOMC import CommandOMC
import OMPython
from org.openmodelica.corba import OMCProxy, SmartProxy
from org.openmodelica.corba.parser import OMCStringParser
from org.openmodelica import ModelicaArray

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
        omcscript= CommandOMC()
        omc= OMCProxy("FTP")
        comando= omcscript.loadFile(self.cbMoFile.selectedItem)
        result = omc.sendExpression(comando)
        comando= omcscript.getClassNames('SmarTSLab.Networks')
        result = omc.sendExpression(comando)
        print 'result OMCProxy', result.__class__.__name__
        print 'result.res', result.res[1:-2]
        listname= result.res[1:-2].split(',')
        for nombre in listname:
            self.cbModel.addItem(nombre)
        
    def onOpenFolder(self, event):
        chooseFile = JFileChooser()
        chooseFile.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        ret = chooseFile.showDialog(self.panel, "Choose folder")
        if ret == JFileChooser.APPROVE_OPTION:
            self.faile= chooseFile.getSelectedFile()
            self.cbOutDir.addItem(self.faile.getPath())
            self.cbOutDir.selectedItem= self.faile.getPath()
            
    def simulateMe(self, event):
        omcscript= CommandOMC()
        omc= OMCProxy("FTP")
        comando= omcscript.loadFile(self.cbMoFile.selectedItem)
    
    def saveResources(self,event):
        config= CtrlProperties()
        config.setmodelPath(self.cbMoFile.selectedItem)
        config.setmodelFile(self.cbMoFile.selectedItem)
        '''TODO Open .mo file, when loaded, and get model names '''
        config.setmodelName(self.cbModel.selectedItem)
        config.setlibraryPath(self.cbMoLib.selectedItem)
        config.setlibraryFile(self.cbMoLib.selectedItem)
        config.setoutputPath(self.cbOutDir.selectedItem)
        config.saveProperties('./res/simParameters.properties', \
                              'Simulation resources')
    
    def saveConfiguration(self,event):
        if self.radioBtn1.isSelected() or self.radioBtn2.isSelected():
            config= PropertiesConfigOMCDY()
            config.setmodelPath(self.cbMoFile.selectedItem)
            config.setmodelFile(self.cbMoFile.selectedItem)
            '''TODO Open .mo file, when loaded, and get model names '''
            config.setmodelName(self.cbModel.selectedItem)
            config.setlibraryPath(self.cbMoLib.selectedItem)
            config.setlibraryFile(self.cbMoLib.selectedItem)
            config.setoutputPath(self.cbOutDir.selectedItem)
        if self.radioBtn3.isSelected():
            config= PropertiesConfigJM()
            
        config.saveProperties('./res/simConfiguration.properties',\
                              'Simulation configuration')
  
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
        self.cbModel = JComboBox(self.dModel)
        simBoton4= JButton('Output Path',actionPerformed=self.onOpenFolder)
        self.dOutPath = []
        self.cbOutDir = JComboBox(self.dOutPath)
        simBoton5= JButton('Simulate',actionPerformed=self.simulateMe)
        simBoton6= JButton('Save Resources',actionPerformed=self.saveResources)
        ''' adding components to the gui '''
        psimures.add(self.cbMoFile)
        psimures.add(simBoton1)
        psimures.add(self.cbMoLib)
        psimures.add(simBoton2)
        psimures.add(self.cbModel)
        psimures.add(simBoton3)
        psimures.add(self.cbOutDir)
        psimures.add(simBoton4)
        psimures.add(simBoton5)
        psimures.add(simBoton6)
        simBoton7= JButton('Save Configuration', actionPerformed= self.saveCongiguration)
        ''' panel model '''
#         simTabPane = JTabbedPane(JTabbedPane.BOTTOM)
        pconfig = JPanel()
        pconfig.setLayout(GridLayout(9,4))
        ''' Configuration Panel '''
        self.label = JLabel('Configuration panel')
        self.radioBtn1 = JRadioButton('OpenModelica')
        self.radioBtn2 = JRadioButton('JModelica')
        self.radioBtn3 = JRadioButton('Dymola')
        self.cbsolver= JComboBox(['dassl','rkfix2'])
        self.cbalgorithm= JComboBox(['AssimuloAlg'])
        self.cboutformat= JComboBox(['.mat','.h5','.csv'])
        self.cbinitialize= JComboBox(['True','False'])
        self.txtinterval= JTextField('0')
        self.txttolerance= JTextField('0')
        self.txtstart= JTextField('0')
        self.txtstop= JTextField('0')
        self.
        ''' adding components to the panel '''
        pconfig.add(self.radioBtn1)
        pconfig.add(self.radioBtn2)
        pconfig.add(self.radioBtn3)
        pconfig.add(JLabel('start time'))
        pconfig.add(self.txtstart)
        pconfig.add(JLabel('start time'))
        pconfig.add(self.txtstop)
        pconfig.add(JLabel('solver'))
        pconfig.add(self.cbsolver)
        pconfig.add(JLabel('algorithm'))
        pconfig.add(self.cbalgorithm)
        pconfig.add(JLabel('interval/ncp'))
        pconfig.add(self.txtinterval)
        pconfig.add(JLabel('tolerance'))
        pconfig.add(self.txttolerance)
        pconfig.add(JLabel('output format'))
        pconfig.add(self.cboutformat)
        pconfig.add(JLabel('Initialize'))
        pconfig.add(self.cbinitialize)
        
#         pOMC.add(pscroll.add(arbol),BorderLayout.LINE_START)
#         simTabPane.addTab("OpenModelica", pOMC)
#         ''' JModelica Panel '''
#         pJM = JPanel(BorderLayout())
#         areatext= JTextArea()
#         areatext.alignmentX = pJM.CENTER_ALIGNMENT
#         pJM.add(areatext, BorderLayout.CENTER)
#         simTabPane.addTab("JModelica", pJM)
#         ''' Dymola Panel '''
#         pDY = JPanel(BorderLayout())
#         areatext= JTextArea()
#         areatext.alignmentX = pDY.CENTER_ALIGNMENT
#         pDY.add(areatext, BorderLayout.CENTER)
#         simTabPane.addTab("Dymola", pDY)
        
        # show the GUI
        splitPane.add(psimures)
        splitPane.add(pconfig);
        frame.add(splitPane)
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        frame.setVisible(True)
            
if __name__ == '__main__':
    MainGUI()
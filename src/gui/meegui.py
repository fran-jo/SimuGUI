'''
Created on 10 jun 2015

@author: fragom
'''
from javax.swing import JPanel, JFrame, JButton, JComboBox, JTextField, JProgressBar
from javax.swing import JSplitPane, JRadioButton, JLabel, ButtonGroup
from javax.swing import JFileChooser, WindowConstants
from javax.swing.filechooser import FileNameExtensionFilter
from java.awt import BorderLayout, Dimension, GridLayout
from java.io import File
from ctrl.ctrlproperties import PrptResources, PrptConfigurationOMCDY, PrptConfigurationJM
from ctrl.commandOMC import CommandOMC
from org.openmodelica.corba import OMCProxy

class MainGUI:
    '''
    TODO: Create a routine to load the values from both .properties
    '''
    def onOpenFile(self, event):
        ''' remember to change the path'''
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
        ''' TODO: Parametrizar este comando '''
        comando= omcscript.getClassNames('SmarTSLab.Models')
        result = omc.sendExpression(comando)
#         print 'result OMCProxy', result.__class__.__name__
#         print 'result.res', result.res[1:-2]
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
        ''' TODO: execute either OMPython or OMCProxy (java) for simulation '''
        omcscript= CommandOMC()
        omc= OMCProxy("Simulate")
        ''' load Modelica '''
        comando= omcscript.loadModelica()
        result = omc.sendExpression(comando)
        ''' load .mo file '''
        comando= omcscript.loadFile(self.cbMoFile.selectedItem)
        result = omc.sendExpression(comando)
        ''' load library '''
        comando= omcscript.loadFile(self.cbMoLib.selectedItem)
        result = omc.sendExpression(comando)
        ''' get the sim options from the properties object '''
        ''' TODO: crear bien el nombre del modelo '''
        strmodel= []
        strmodel.append('SmarTSLab.Models.')
        strmodel.append(self.cbModel.selectedItem)
        comando= omcscript.simulate(''.join(strmodel), self.config.getProperties(), False)
        result = omc.sendExpression(comando)
        ''' TODO: Get the result file and save it to output dir'''
        ''' TODO: incluir rutina para guardar formato en .h5, clase addicional a PhasorMeasH5'''
        print result.res
    
    def saveResources(self,event):
        self.config= PrptResources()
        self.config.setmodelPath(self.cbMoFile.selectedItem)
        self.config.setmodelFile(self.cbMoFile.selectedItem)
        self.config.setmodelName(self.cbModel.selectedItem)
        self.config.setlibraryPath(self.cbMoLib.selectedItem)
        self.config.setlibraryFile(self.cbMoLib.selectedItem)
        self.config.setoutputPath(self.cbOutDir.selectedItem)
        if self.radioBtnOMC.isSelected():
            nomfile= './config/simParametersOMC.properties'
        if self.radioBtnJM.isSelected():
            nomfile= './config/simParametersJM.properties'
        if self.radioBtnDY.isSelected():
            nomfile= './config/simParametersDY.properties'
        self.config.saveProperties(nomfile, 'Simulation resources')
    
    def saveConfiguration(self,event):
        if self.radioBtnOMC.isSelected() or self.radioBtnDY.isSelected():
            self.config= PrptConfigurationOMCDY()
            self.config.setstarttime(self.txtstart.getText())
            self.config.setstoptime(self.txtstop.getText())
            self.config.settolerance(self.txttolerance.getText())
            self.config.setintervals(self.txtinterval.getText())
            self.config.setmethod(self.cbsolver.selectedItem)
            self.config.setoutputformat(self.cboutformat.selectedItem)
            if self.radioBtnOMC.isSelected():
                nomfile= './config/simConfigurationOMC.properties'
            if self.radioBtnDY.isSelected():
                nomfile= './config/simConfigurationDY.properties'
            self.config.saveProperties(nomfile, 'Simulation Configuration')
        if self.radioBtnJM.isSelected():
            self.config= PrptConfigurationJM()
            self.config.setstarttime(self.txtstart.getText())
            self.config.setstoptime(self.txtstop.getText())
            self.config.setintervals(self.txtinterval.text)
            self.config.setmethod(self.cbsolver.selectedItem)
            self.config.setalgorithm(self.cbalgorithm.selectedItem)
            self.config.setinitialization(self.cbinitialize.selectedItem)
            nomfile= './config/simConfigurationJM.properties'
            self.config.saveProperties(nomfile, 'Simulation Configuration')
        self.bSimulation.enabled= 1
  
    def __init__(self):
        self.open= False
        self.panel = JPanel()
        self.panel.setLayout(BorderLayout())
        frame = JFrame("GUI Development ")
        frame.setSize(800, 600)
        frame.setLayout(BorderLayout())
        splitPane = JSplitPane(JSplitPane.VERTICAL_SPLIT)
        
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
        bsaveSource= JButton('Save Resources',actionPerformed=self.saveResources)
        ''' adding components to the gui '''
        psimures.add(self.cbMoFile)
        psimures.add(simBoton1)
        psimures.add(self.cbMoLib)
        psimures.add(simBoton2)
        psimures.add(self.cbModel)
        psimures.add(simBoton3)
        psimures.add(self.cbOutDir)
        psimures.add(simBoton4)
        psimures.add(bsaveSource)
        bSaveCfg= JButton('Save Configuration', actionPerformed= self.saveConfiguration)
        self.bSimulation= JButton('Simulate', actionPerformed= self.simulateMe)
        self.bSimulation.enabled= 0
        ''' panel model '''
#         simTabPane = JTabbedPane(JTabbedPane.BOTTOM)
        pconfig = JPanel()
        pconfig.setLayout(GridLayout(9,4))
        ''' Configuration Panel '''
        self.label = JLabel('Configuration panel')
        self.radioBtnOMC = JRadioButton('OpenModelica')
        self.radioBtnJM = JRadioButton('JModelica')
        self.radioBtnDY = JRadioButton('Dymola')
        self.cbsolver= JComboBox(['dassl','rkfix2'])
        self.cbalgorithm= JComboBox(['AssimuloAlg'])
        self.cboutformat= JComboBox(['.mat','.h5','.csv'])
        self.cbinitialize= JComboBox(['True','False'])
        self.txtinterval= JTextField('0')
        self.txttolerance= JTextField('0')
        self.txtstart= JTextField('0')
        self.txtstop= JTextField('0')
        self.lblResult= JLabel('Simulation information')
        simProgress= JProgressBar()
        ''' adding components to the panel '''
        pconfig.add(self.radioBtnOMC)
        pconfig.add(self.radioBtnJM)
        pconfig.add(self.radioBtnDY)
        rbBtnGroup = ButtonGroup()
        rbBtnGroup.add(self.radioBtnOMC)
        rbBtnGroup.add(self.radioBtnJM)
        rbBtnGroup.add(self.radioBtnDY)
        pconfig.add(JLabel('Start time'))
        pconfig.add(self.txtstart)
        pconfig.add(JLabel('Stop time'))
        pconfig.add(self.txtstop)
        pconfig.add(JLabel('Solver'))
        pconfig.add(self.cbsolver)
        pconfig.add(JLabel('Algorithm (JM)'))
        pconfig.add(self.cbalgorithm)
        pconfig.add(JLabel('Interval'))
        pconfig.add(self.txtinterval)
        pconfig.add(JLabel('Tolerance'))
        pconfig.add(self.txttolerance)
        pconfig.add(JLabel('Output format'))
        pconfig.add(self.cboutformat)
        pconfig.add(JLabel('Initialize (JM)'))
        pconfig.add(self.cbinitialize)
        pconfig.add(bSaveCfg)
        pconfig.add(self.bSimulation)
        pconfig.add(self.lblResult)
        pconfig.add(simProgress)
        
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
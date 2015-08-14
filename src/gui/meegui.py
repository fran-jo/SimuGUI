'''
Created on 10 jun 2015

@author: fragom
'''
from java.lang import Runnable
from javax.swing import JPanel, JFrame, JButton, JComboBox, JTextField, JProgressBar
from javax.swing import SwingWorker, SwingUtilities
from javax.swing import JSplitPane, JRadioButton, JLabel, ButtonGroup
from javax.swing import JFileChooser, WindowConstants
from javax.swing.filechooser import FileNameExtensionFilter
from java.awt import BorderLayout, Dimension, GridBagLayout, GridBagConstraints
from java.awt import Cursor as awtCursor
from java.io import File
from ctrl.ctrlresources import ParameterResources
from ctrl.ctrlsimulation import SimulationConfigOMCDY, SimulationConfigJM
from ctrl.commandOMC import CommandOMC
from org.openmodelica.corba import OMCProxy
from java.beans import PropertyChangeListener

class SimulationTask(SwingWorker):
    
    def __init__(self, gui):
        self.gui = gui
        SwingWorker.__init__(self)
#         super(self)
  
    def doInBackground(self):
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
        strmodel= []
        strmodel.append('SmarTSLab.Models.')
        strmodel.append(self.cbModel.selectedItem)
        comando= omcscript.simulate(''.join(strmodel), self.config.getProperties(), False)
        print '1) simulate ', comando
        result = omc.sendExpression(comando)
        print result.res
        ''' TODO: Get the result file and save it to output dir'''
        ''' TODO: incluir rutina para guardar formato en .h5, clase addicional a PhasorMeasH5'''
        print result.res
        
    def process(self):
        print 'swing worker process method'
        
    def done(self):
        print 'swing worker done method'

class ResourcePanel(JPanel):
    
    def __init__(self):
        ''' Resources Panel '''
#         psimures= JPanel(GridBagLayout())
#         psimures.setSize(Dimension(500,300))
        self.setLayout(GridBagLayout())
#         super(self,GridBagLayout())
        self.setSize(Dimension(500,300))
        ''' fila 1 '''
        label = JLabel('Resources panel')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 1
        c.gridwidth = 4
        c.gridx = 0
        c.gridy = 0
        self.add(label, c)
        ''' fila 2 '''
        self.dModelFile = []
        self.cbMoFile = JComboBox(self.dModelFile)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.75
        c.gridwidth = 3
        c.gridx = 0
        c.gridy = 1
        self.add(self.cbMoFile, c)
        bloadmodel= JButton('Load Model',actionPerformed=self.onOpenFile)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.25
#         c.gridwidth = 1
        c.gridx = 3
        c.gridy = 1
        self.add(bloadmodel, c)
        ''' fila 3 '''
        self.dLibFile = []
        self.cbMoLib = JComboBox(self.dLibFile)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.75
        c.gridwidth = 3
        c.gridx = 0
        c.gridy = 2
        self.add(self.cbMoLib, c)
        bloadlib= JButton('Load Library',actionPerformed=self.onOpenFile)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.25
#         c.gridwidth = 1
        c.gridx = 3
        c.gridy = 2
        self.add(bloadlib, c)
        ''' fila 4 '''
        self.dModel = []
        self.cbModel = JComboBox(self.dModel)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.75
        c.gridwidth = 3
        c.gridx = 0
        c.gridy = 3
        self.add(self.cbModel, c)
        bselectmodel= JButton('Select Model',actionPerformed=self.onOpenModel)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.25
#         c.gridwidth = 1
        c.gridx = 3
        c.gridy = 3
        self.add(bselectmodel, c)
        ''' fila 5 '''
        self.dOutPath = []
        self.cbOutDir = JComboBox(self.dOutPath)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.75
        c.gridwidth = 3
        c.gridx = 0
        c.gridy = 4
        self.add(self.cbOutDir, c)
        bloadoutpath= JButton('Output Path',actionPerformed=self.onOpenFolder)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.25
#         c.gridwidth = 1
        c.gridx = 3
        c.gridy = 4
        self.add(bloadoutpath, c)
        ''' fila 6 '''
        bsaveSource= JButton('Save Resources',actionPerformed=self.saveResources)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridwidth = 2
        c.gridx = 0
        c.gridy = 5
        self.add(bsaveSource, c)
        bloadSource= JButton('Load Resources',actionPerformed=self.loadResources)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridwidth = 2
        c.gridx = 2
        c.gridy = 5
        self.add(bloadSource, c)
    
    def onOpenFile(self, event):
        ''' remember to change the path'''
        chooseFile = JFileChooser()
        chooseFile.setCurrentDirectory(File('C:\Users\fragom\PhD_CIM\Modelica\Models')) 
        filtro = FileNameExtensionFilter("mo files", ["mo"])
        chooseFile.addChoosableFileFilter(filtro)
        ret = chooseFile.showDialog(self, "Choose file")
        if ret == JFileChooser.APPROVE_OPTION:
            self.faile= chooseFile.getSelectedFile()
            if event.getActionCommand() == "Load Model":
                self.cbMoFile.addItem(self.faile.getPath())
                self.cbMoFile.selectedItem= self.faile.getPath()
            if event.getActionCommand() == "Load Library":
                self.cbMoLib.addItem(self.faile.getPath())
                self.cbMoLib.selectedItem= self.faile.getPath()
#             print self.faile
    
    def onOpenModel(self, event):
        omcscript= CommandOMC()
        omc= OMCProxy("FTP")
        comando= omcscript.loadFile(self.cbMoFile.selectedItem)
        result = omc.sendExpression(comando)
        ''' TODO: Parametrizar este comando '''
        modelname=  self.cbMoFile.selectedItem.split('\\')
#         print modelname[-1].split('.')[0]
        modelname= modelname[-1].split('.')[0]
        comando= omcscript.getClassNames(modelname)
        result = omc.sendExpression(comando)
#         print 'result OMCProxy', result.__class__.__name__
#         print 'result.res', result.res[1:-2]
        listname= result.res[1:-2].split(',')
        for nombre in listname:
            self.cbModel.addItem(nombre)
        
    def onOpenFolder(self, event):
        chooseFile = JFileChooser()
        chooseFile.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        ret = chooseFile.showDialog(self, "Choose folder")
        if ret == JFileChooser.APPROVE_OPTION:
            self.faile= chooseFile.getSelectedFile()
            self.cbOutDir.addItem(self.faile.getPath())
            self.cbOutDir.selectedItem= self.faile.getPath()
    
    def saveResources(self,event):
        self.config= ParameterResources()
        self.config.set_modelPath(self.cbMoFile.selectedItem)
        self.config.set_modelFile(self.cbMoFile.selectedItem)
        self.config.set_modelName(self.cbModel.selectedItem)
        self.config.set_libraryPath(self.cbMoLib.selectedItem)
        self.config.set_libraryFile(self.cbMoLib.selectedItem)
        self.config.set_outputPath(self.cbOutDir.selectedItem)
        nomfile= './config/simParameters.properties'
        self.config.save_Properties(nomfile, 'Simulation resources')
    
    def loadResources(self,event):
        self.config= ParameterResources()
        nomfile= './config/simParameters.properties'
        self.config.load_Properties(nomfile)
        self.cbMoFile.addItem(self.config.get_modelFile())
        self.cbMoFile.selectedItem= self.config.get_modelFile()
        self.cbMoLib.addItem(self.config.get_libraryFile())
        self.cbMoLib.selectedItem= self.config.get_libraryFile()
        self.cbModel.addItem(self.config.get_modelName())
        self.cbModel.selectedItem= self.config.get_modelName()
        self.cbOutDir.addItem(self.config.get_outputPath())
        self.cbOutDir.selectedItem= self.config.get_outputPath()
        

class ConfigurationPanel(JPanel, PropertyChangeListener):
    
    def __init__(self):
        ''' Configuration Panel '''
#         pconfig = JPanel(GridBagLayout())
#         pconfig.setSize(Dimension(500,300))
        self.setLayout(GridBagLayout())
#         super(self,GridBagLayout())
        self.setSize(Dimension(500,300))
        ''' fila 1 '''
        label = JLabel('Configuration panel')
        c1 = GridBagConstraints()
        c1.fill = GridBagConstraints.HORIZONTAL
        c1.weightx = 0.5
        c1.gridwidth = 4
        c1.gridx = 0
        c1.gridy = 0
        self.add(label, c1)
        ''' fila 2 '''
        self.radioBtnOMC = JRadioButton('OpenModelica')
        c2 = GridBagConstraints()
        c2.fill = GridBagConstraints.HORIZONTAL
        c2.weightx = 0.5
        c2.gridx = 0
        c2.gridy = 1
        self.add(self.radioBtnOMC, c2)
        self.radioBtnJM = JRadioButton('JModelica')
        c3 = GridBagConstraints()
        c3.fill = GridBagConstraints.HORIZONTAL
        c3.weightx = 0.5
        c3.gridx = 1
        c3.gridy = 1
        self.add(self.radioBtnJM, c3)
        self.radioBtnDY = JRadioButton('Dymola')
        c4 = GridBagConstraints()
        c4.fill = GridBagConstraints.HORIZONTAL
        c4.weightx = 0.5
        c4.gridx = 2
        c4.gridy = 1
        self.add(self.radioBtnDY, c4)
        rbBtnGroup = ButtonGroup()
        rbBtnGroup.add(self.radioBtnOMC)
        rbBtnGroup.add(self.radioBtnJM)
        rbBtnGroup.add(self.radioBtnDY)
        ''' fila 2 '''
        label = JLabel('Start time')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 0
        c.gridy = 2
        self.add(label, c)
        self.txtstart= JTextField('0')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 1
        c.gridy = 2
        self.add(self.txtstart, c)
        label = JLabel('Stop time')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 2
        c.gridy = 2
        self.add(label, c)
        self.txtstop= JTextField('0')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 3
        c.gridy = 2
        self.add(self.txtstop, c)
        ''' fila 3 '''
        label = JLabel('Solver')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 0
        c.gridy = 3
        self.add(label, c)
        self.cbsolver= JComboBox(['dassl','rkfix2'])
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 1
        c.gridy = 3
        self.add(self.cbsolver, c)
        label = JLabel('Algorithm (JM)')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 2
        c.gridy = 3
        self.add(label, c)
        self.cbalgorithm= JComboBox(['AssimuloAlg'])
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 3
        c.gridy = 3
        self.add(self.cbalgorithm, c)
        ''' fila 4 '''
        label = JLabel('Interval')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 0
        c.gridy = 4
        self.add(label, c)
        self.txtinterval= JTextField('0')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 1
        c.gridy = 4
        self.add(self.txtinterval, c)
        ''' fila 5 '''
        label = JLabel('Tolerance')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 0
        c.gridy = 5
        self.add(label, c)
        self.txttolerance= JTextField('0')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 1
        c.gridy = 5
        self.add(self.txttolerance, c)
        ''' fila 6 '''
        label = JLabel('Output format')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 0
        c.gridy = 6
        self.add(label, c)
        self.cboutformat= JComboBox(['.mat','.h5','.csv'])
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 1
        c.gridy = 6
        self.add(self.cboutformat, c)
        label = JLabel('Initialize (JM)')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 2
        c.gridy = 6
        self.add(label, c)
        self.cbinitialize= JComboBox(['True','False'])
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridx = 3
        c.gridy = 6
        self.add(self.cbinitialize, c)
        ''' fila 7 '''
        bSaveCfg= JButton('Save Configuration', actionPerformed= self.saveConfiguration)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridwidth = 2
        c.gridx = 0
        c.gridy = 7
        self.add(bSaveCfg, c)
        self.bSimulation= JButton('Load Configuration', actionPerformed= self.loadConfiguration)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 0.5
        c.gridwidth = 2
        c.gridx = 2
        c.gridy = 7
        self.add(self.bSimulation, c)
        ''' fila 8 '''
        self.bSimulation= JButton('Simulate', actionPerformed= self.startSimlation)
        self.bSimulation.enabled= 0
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 1
        c.gridwidth = 4
        c.gridx = 0
        c.gridy = 8
        self.add(self.bSimulation, c)
        ''' file 9 '''
        simProgress= JProgressBar(0, self.getWidth(), value=0, stringPainted=True)
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 1
        c.gridwidth = 4
        c.gridx = 0
        c.gridy = 9
        self.add(simProgress, c)
        ''' fila 10 '''
        self.lblResult= JLabel('Simulation information')
        c = GridBagConstraints()
        c.fill = GridBagConstraints.HORIZONTAL
        c.weightx = 1
        c.gridwidth = 4
        c.gridx = 0
        c.gridy = 10
        self.add(self.lblResult, c) 
     
    def startSimlation(self, event):
        "Invoked when the user presses the start button"
        self.bSimulation.enabled = False
        #Instances of javax.swing.SwingWorker are not reusable, so
        #we create new instances as needed.
        self.simtask = SimulationTask(self)
#         self.simtask.addPropertyChangeListener(self)
        self.simtask.execute() 
        
    def saveConfiguration(self,event):
        if self.radioBtnOMC.isSelected() or self.radioBtnDY.isSelected():
            self.config= SimulationConfigOMCDY()
            self.config.set_starttime(self.txtstart.getText())
            self.config.set_stoptime(self.txtstop.getText())
            self.config.set_tolerance(self.txttolerance.getText())
            self.config.set_intervals(self.txtinterval.getText())
            self.config.set_method(self.cbsolver.selectedItem)
            self.config.set_outputformat(self.cboutformat.selectedItem)
            if self.radioBtnOMC.isSelected():
                nomfile= './config/simConfigurationOMC.properties'
            if self.radioBtnDY.isSelected():
                nomfile= './config/simConfigurationDY.properties'
            self.config.save_Properties(nomfile, 'Simulation Configuration')
        if self.radioBtnJM.isSelected():
            self.config= SimulationConfigJM()
            self.config.set_starttime(self.txtstart.getText())
            self.config.set_stoptime(self.txtstop.getText())
            self.config.set_intervals(self.txtinterval.text)
            self.config.set_method(self.cbsolver.selectedItem)
            self.config.set_algorithm(self.cbalgorithm.selectedItem)
            self.config.set_initialization(self.cbinitialize.selectedItem)
            self.config.set_outputformat(self.cboutformat.selectedItem)
            nomfile= './config/simConfigurationJM.properties'
            self.config.save_Properties(nomfile, 'Simulation Configuration')
        self.bSimulation.enabled= 1
        
    def loadConfiguration(self, event):
        if self.radioBtnOMC.isSelected() or self.radioBtnDY.isSelected():
            self.config= SimulationConfigOMCDY()
            self.config.load_Properties('./config/simConfigurationOMC.properties')
            self.txtstart.setText(self.config.get_starttime())
            self.txtstop.setText(self.config.get_stoptime())
            self.txttolerance.setText(self.config.get_tolerance())
            self.txtinterval.setText(self.config.get_intervals())
            self.cbsolver.selectedItem= self.config.get_method()
            self.cboutformat.selectedItem= self.config.get_outputformat()
        if self.radioBtnJM.isSelected():
            self.config= SimulationConfigJM()
            self.config.load_Properties('./config/simConfigurationJM.properties')
            self.txtstart.setText(self.config.get_starttime())
            self.txtstop.setText(self.config.get_stoptime())
            self.txtinterval.setText(self.config.get_intervals())
            self.cbsolver.selectedItem= self.config.get_method()
            self.cbalgorithm.selectedItem= self.config.get_algorithm()
            self.cbinitialize.selectedItem= self.config.get_initialization()
#             self.cboutformat.selectedItem= self.config.get_outputformat()
        self.bSimulation.enabled= 1
        
###########################################################################        
def createAndShowGUI():
    # Create the GUI and show it. As with all GUI code, this must run
    # on the event-dispatching thread.
    frame = JFrame("GUI Development ")
    frame.setSize(500, 600)
    frame.setLayout(BorderLayout())
    splitPane = JSplitPane(JSplitPane.VERTICAL_SPLIT)
    
    #Create and set up the content pane.
    psimures= ResourcePanel()
    psimures.setOpaque(True)
    pconfig = ConfigurationPanel()
    pconfig.setOpaque(True)      #content panes must be opaque

    # show the GUI
    splitPane.add(psimures)
    splitPane.add(pconfig)
    frame.add(splitPane)
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
    ''' TODO: load the current configuration from resources.properties and 
    configuration.properties '''
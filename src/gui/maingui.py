'''
Created on 10 jun 2015

@author: fragom
'''
from javax.swing import JPanel, JMenu, JMenuItem, JMenuBar, JFrame, JTree,\
    JTextArea
from javax.swing import JSplitPane, JTabbedPane, JLabel, JScrollPane
from javax.swing import JFileChooser, WindowConstants
from javax.swing.filechooser import FileNameExtensionFilter
from java.awt import BorderLayout, Dimension

def onClick(self, e):
    chooseFile = JFileChooser()
    filtro = FileNameExtensionFilter("c files", ["c"])
    chooseFile.addChoosableFileFilter(filtro)
    ret = chooseFile.showDialog(self.panel, "Choose file")
    if ret == JFileChooser.APPROVE_OPTION:
        faile= chooseFile.getSelectedFile()
        print faile
            
if __name__ == '__main__':
    panel = JPanel()
    panel.setLayout(BorderLayout())
    frame = JFrame("GUI Development ")
    frame.setSize(800, 600)
    frame.setLayout(BorderLayout())
    splitPane = JSplitPane(JSplitPane.VERTICAL_SPLIT);
    
    # Create the menu
    '''Menu File'''
    jMenuBar1 = JMenuBar()
    jMenu1 = JMenu()
    jMenu1.setText('File')
    jMenuItem1 = JMenuItem('Open', actionPerformed= onClick)
    jMenuItem2 = JMenuItem()
    jMenuItem2.setText('Exit')
    jMenu1.add(jMenuItem1)
    jMenu1.add(jMenuItem2)
    '''Menu Simulation'''
    jMenu2 = JMenu()
    jMenu2.setText('Simulation')
    jMenuItem21 = JMenuItem('Simulation Options')
    jMenuItem22 = JMenuItem('Simulate')
    jMenuItem23 = JMenuItem('Generate FMU')
    jMenu2.add(jMenuItem21)
    jMenu2.add(jMenuItem22)
    jMenu2.add(jMenuItem23)
    '''Add menu to menu bar and frame'''
    jMenuBar1.add(jMenu1)
    jMenuBar1.add(jMenu2)
    frame.setJMenuBar(jMenuBar1)
    
    # Create main tab panel
    tabPane = JTabbedPane(JTabbedPane.TOP)
    ''' panel model '''
    label = JLabel("<html><br>This is a tab1</html>")
    pModel = JPanel()
    pModel.setLayout(BorderLayout())
    pscroll= JScrollPane()
    ''' inside panel model '''
    arbol= JTree()
    arbol.setPreferredSize(Dimension(200,500))
    pModel.add(label,BorderLayout.PAGE_START)
    pModel.add(pscroll.add(arbol),BorderLayout.LINE_START)
    tabPane.addTab("Model View", pModel)
    ''' panel results '''
    panelRes = JPanel(BorderLayout())
    areatext= JTextArea()
    areatext.alignmentX = panelRes.CENTER_ALIGNMENT
    panelRes.add(areatext, BorderLayout.CENTER)
    tabPane.addTab("Results View", panelRes)
    splitPane.setRightComponent(tabPane);
    
    # show the GUI
    frame.add(splitPane)
    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    frame.setVisible(True)
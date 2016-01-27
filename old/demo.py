"""\
Create a panel showing all of the colors defined in the pawt.colors module
Display the names of bright colors in black and of dark colors in white
"""
from javax.swing import *
from java.awt import *
from java.awt import Color
from javax.swing import ImageIcon
from javax.swing import JFrame
from javax.swing import *
from java.awt import *
# from default.example6 import Example1
from javax.swing import JFileChooser
from javax.swing.filechooser import FileNameExtensionFilter





class Example:
  def onClick(self, e):
      chooseFile = JFileChooser()
      filter = FileNameExtensionFilter("c files", ["c"])
      chooseFile.addChoosableFileFilter(filter)
      ret = chooseFile.showDialog(self.panel, "Choose file")
      if ret == JFileChooser.APPROVE_OPTION:
            file = chooseFile.getSelectedFile()
            
            print file
        
  
  def copyText(self,event):
      self.textarea.text = self.textfield1.text
  def writeText(self,event):
      self.textarea.text = Example1()
      #print self.textfield1.text 
       
  def __init__(self):
    self.panel = JPanel()
    self.panel.setLayout(BorderLayout())
    frame = JFrame("GUI Development ")
    frame.setSize(800, 600)
    frame.setLayout(BorderLayout())

    splitPane = JSplitPane(JSplitPane.VERTICAL_SPLIT);

    self.textfield1 = JTextField('Type something here')
    self.textfield1.setColumns(40);
    #self.textfield1.setRows(5);
    #self.textfield2 = JTextField('Dont write anythong',30)
    label1 = JLabel("Command:")
    panel1 = JPanel()
    '''
    '''
    jMenuBar1 = JMenuBar()
    jMenu1 = JMenu()
    jMenu2 = JMenu()
    jMenuItem1 = JMenuItem('Open', actionPerformed=self.onClick)
    jMenuItem2 = JMenuItem()
    jMenu1.setText('File')
    jMenu2.setText('Simulation')
    
    #jMenuItem1.setText('Open')
    jMenuItem2.setText('Exit')
    jMenu1.add(jMenuItem1)
    jMenu1.add(jMenuItem2)
    jMenuBar1.add(jMenu1)
    
    jMenuItem21 = JMenuItem('Simulation Options',actionPerformed=self.writeText)
    jMenuItem22 = JMenuItem('Simulate',actionPerformed=self.writeText)
    jMenuItem23 = JMenuItem('Generate FMU',actionPerformed=self.writeText)
    
#     jMenuItem21.setText('Run Project')
#     jMenuItem22.setText('Generate FMU')
    jMenu2.add(jMenuItem21)
    jMenu2.add(jMenuItem22)
    jMenu2.add(jMenuItem23)
    jMenuBar1.add(jMenu2)
    frame.setJMenuBar(jMenuBar1)
    
    '''
    '''
    panel1.add(label1,BorderLayout.WEST)
    panel1.add(self.textfield1, BorderLayout.CENTER)
    copyButton = JButton('send',actionPerformed=self.copyText)
    panel1.add(copyButton, BorderLayout.EAST)
    #panel1.add(self.textfield2, BorderLayout.SOUTH)
    splitPane.setLeftComponent(panel1);
    '''
    
   image adding in the frame
    
    
    '''
    
    #imPanel.add(imPanel,BorderLayout.WEST)
    #imPanel.setBackground(Color(66, 66, 66))
    imPanel1 = JPanel()
    rot = ImageIcon("ballon.jpg")
    rotLabel = JLabel(rot)
    rotLabel.setBounds(0,0, rot.getIconWidth(), rot.getIconHeight())
    imPanel1.add(rotLabel, BorderLayout.SOUTH)
    frame.add(imPanel1, BorderLayout.SOUTH)
    
    '''
    panel for text area adding in split pan 
    
    '''
    tabPane = JTabbedPane(JTabbedPane.TOP)

    label = JLabel("<html><br>This is a tab1</html>")
    panel1 = JPanel()
    panel1.setBackground(Color.lightGray)
    panel23 = JPanel()
    panel23.setBackground(Color.black)
    panel1.add(panel23,BorderLayout.SOUTH)
    panel1.add(label,BorderLayout.NORTH)
    '''
    adding button in the panel1
    '''
    writeButton = JButton('write')
    panel1.add(writeButton, BorderLayout.WEST)
    tabPane.addTab("tab1", panel1)
    
    
    #frame.add(panel1,BorderLayout.EAST)
    #panel1.setBackground(Color(66, 66, 66))
#     rot1 = ImageIcon("ballon.jpg",BorderLayout.SOUTH)
#     rotLabel1 = JLabel(rot1)
#     rotLabel1.setBounds(0,0, rot.getIconWidth(), rot.getIconHeight())
#     panel1.add(rotLabel1)

    label2 = JLabel("This is a tab2")

    panel2 = JPanel()
    panel2.setBackground(Color.lightGray)
    panel2.add(label2)
    tabPane.addTab("tab2", panel2)

#     imPanel2 =JPanel()
    self.textarea = JTextArea('Write something from commandLine')
    self.textarea.setColumns(40);
    self.textarea.setRows(40);
 
    panel2.add(self.textarea, BorderLayout.NORTH)

    splitPane.setRightComponent(tabPane);
    splitPane.setDividerLocation(60);

    frame.add(splitPane)
    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    frame.setVisible(True)

if __name__ == '__main__':
    Example()
    
    
    

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as PlotFig

from matplotlib import rcParams
from PyQt4.QtGui import QFormLayout
rcParams['font.size'] = 9

class MatplotlibWidget(FigureCanvas):
    """
    MatplotlibWidget inherits PyQt4.QtGui.QWidget
    and matplotlib.backend_bases.FigureCanvasBase
    
    Options: option_name (default_value)
    -------    
    parent (None): parent widget
    title (''): figure title
    xlabel (''): X-axis label
    ylabel (''): Y-axis label
    xlim (None): X-axis limits ([min, max])
    ylim (None): Y-axis limits ([min, max])
    xscale ('linear'): X-axis scale
    yscale ('linear'): Y-axis scale
    width (4): width in inches
    height (3): height in inches
    dpi (100): resolution in dpi
    hold (False): if False, figure will be cleared each time plot is called
    
    Widget attributes:
    -----------------
    figure: instance of matplotlib.figure.Figure
    axes: figure axes
    """    
    def __init__(self, parent=None, title='Title', xlabel='x label', ylabel='y label', 
                width= 100, height= 100, dpi=100):
        super(MatplotlibWidget, self).__init__(Figure())

        self.setParent(parent)
        self.figure= PlotFig.figure(figsize=(width, height), dpi=dpi) 
        #self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        #self.canvas.setParent(parent)
        #self.canvas.setFocusPolicy(Qt.StrongFocus)
        #self.canvas.setFocus()
        self.grafica = self.figure.add_subplot(111) 
        self.grafica.set_title(title, fontsize=12)
        self.grafica.set_xlabel(xlabel, fontsize=10)
        self.grafica.set_ylabel(ylabel, fontsize=10)
        self.grafica.grid()
        self.toolbar= NavigationToolbar(self.canvas, self)
        self.toolbar.setParent(parent)
        vboxtab= QFormLayout()
        vboxtab.addWidget(self.canvas)
        vboxtab.addWidget(self.toolbar)
        parent.setLayout(vboxtab)
        #Canvas.setSizePolicy(self, QSizePolicy.Minimum, QSizePolicy.Minimum)
        #FigureCanvas.updateGeometry(self)

#     def setLayout(self, widgentparent, height, width):
#         vboxtabSim= QVBoxLayout()
#         vboxtabSim.addWidget(self.figure)
#         vboxtabSim.addWidget(self.toolbar)
#         widgentparent.setLayout(vboxtabSim)
#         widgentparent.setFixedWidth(width)
#         widgentparent.setFixedHeight(height)
    
    def plot(self, x, y, title='Title', xlabel='x label', ylabel='y label', c= 'b', marker= 'o', hold= False):
        if not hold:
            self.grafica.clear()
        self.grafica.plot(x,y)
        self.grafica.set_title(title, fontsize=12)
        self.grafica.set_xlabel(xlabel, fontsize=10)
        self.grafica.set_ylabel(ylabel, fontsize=10)
        self.grafica.grid()
        self.draw()  
    
    def scatter(self, x, y, title='Title', xlabel='x label', ylabel='y label', c= 'b', marker= 'o', hold= False):
        self.grafica = self.figure.add_subplot(111)   
#         if not hold:
#             self.grafica.clear()
        self.grafica.scatter(x,y, c=c, marker=marker)
        self.grafica.set_title(title, fontsize=12)
        self.grafica.set_xlabel(xlabel, fontsize=10)
        self.grafica.set_ylabel(ylabel, fontsize=10)
        self.grafica.grid()
        self.draw()
        
    def clear(self):
        self.grafica.cla()
        self.grafica.grid()
        self.draw()

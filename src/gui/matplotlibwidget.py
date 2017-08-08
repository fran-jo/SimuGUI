from PyQt4.QtGui import QSizePolicy

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

from matplotlib import rcParams
rcParams['font.size'] = 9

class MatplotlibWidget(Canvas):
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
                width= 100, height= 100, dpi=100, hold=False):
        super(MatplotlibWidget, self).__init__(Figure())

        self.setParent(parent)
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = Canvas(self.figure)
        self.theplot = self.figure.add_subplot(111)       
        self.theplot.set_title(title, fontsize=12)
        self.theplot.set_xlabel(xlabel, fontsize=10)
        self.theplot.set_ylabel(ylabel, fontsize=10)
        self.theplot.grid()
        
        #Canvas.setSizePolicy(self, QSizePolicy.Minimum, QSizePolicy.Minimum)
        Canvas.updateGeometry(self)

    def plot(self, x, y, hold= False):
        self.theplot.plot(x,y)
        self.theplot.grid()
        self.draw()  
        self.theplot.hold(hold)          

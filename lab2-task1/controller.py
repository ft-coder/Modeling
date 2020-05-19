import pyqtgraph
import sys
import numpy
from PyQt5 import QtWidgets, QtCore
from model import Ui_Form

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.createButt.clicked.connect(self.create_plot)
        self.ui.clearButt.clicked.connect(self.clear_plot)
        self.ui.graphicsView.setBackground(background='w')
        self.ui.graphicsView.showGrid(x=True, y=True)

    def gen_plots(self, p, m):
        x_arr = numpy.arange(0, p, 0.01)
        Q = []
        for x in x_arr:
            if x < 1:
                q = x/(1-x**(m+2))*(1+x**(m+1)*(m*x-m+x-2))/(1-x)
            elif x == 1:
                q = ((m+1)/2)*x
            else:
                q = x/(1-x**(m+2))*(1+x**(m+1)*(m*x-m+x-2))/(1-x)
            Q.append(q)
        return {"x": x_arr, "y": Q}

    def create_plot(self):
        p = float(self.ui.p_Edit.text())
        m = float(self.ui.m_Edit.text())
        points = self.gen_plots(p, m)
        pen_style = pyqtgraph.mkPen('r', width=2)
        self.ui.graphicsView.plot(points["x"], points["y"], pen=pen_style)

    def clear_plot(self):
        self.ui.graphicsView.clear()

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

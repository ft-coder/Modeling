import pyqtgraph
import sys
import numpy as np
import random
import math
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

    def gen_plots(self, a, b, intervals, numbers, lamb):
        f = (b - a) / intervals
        L = []
        xdata = list(np.arange(a, b, f))
        x = [i for i in np.arange(a, b, 0.1)]
        y = [lamb * math.exp(-lamb * i) for i in x]
        ydata = []
        for i in xdata:
            for j in x:
                if i == j:
                    index = x.index(j)
                    ydata.append(y[index])
        return {"x": x, "y": y, "xdata": xdata, "ydata": ydata, "width": f}

    def create_plot(self):
        a = float(self.ui.aEdit.text())
        b = float(self.ui.bEdit.text())
        intervals = float(self.ui.intervals.text())
        lamb = float(self.ui.lambdaEdit.text())
        numbers = float(self.ui.numbers.text())
        '''a = 0.0
        b = 10.0
        intervals = 10.0
        lamb = 0.5
        numbers = 500'''
        points = self.gen_plots(a, b, intervals, numbers, lamb)
        bar = pyqtgraph.BarGraphItem(x=points["xdata"], height=points["ydata"],
                                     width=points["width"], brush='g')
        self.ui.graphicsView.addItem(bar)
        pen_style = pyqtgraph.mkPen('g', width=2)
        self.ui.graphicsView.plot(points["x"], points["y"], pen="b")

    def clear_plot(self):
        self.ui.graphicsView.clear()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

import pyqtgraph
import sys
import numpy
import random
from PyQt5 import QtWidgets, QtCore
import math
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

    @staticmethod
    def create_random(l):
        return -(math.log(random.random()) / l)

    @staticmethod  # ((l ** k) * (x ** (k - 1)) * math.exp(-l * x)) / math.factorial(k - 1)
    def function(x, k, l):
        return (l ** k) * (x ** (k - 1)) * math.exp(-l * x) / math.factorial(k - 1)

    def gen_plots(self, n, k, t, l):
        x_arr = numpy.arange(0, 50, 0.1)
        y_arr = [self.function(x, k, l) for x in x_arr]

        gista_y = []
        gista_x = []
        for x in numpy.arange(0, 50, t):
            y = self.function(x, k, l)
            gista_y.append(y)
            gista_x.append(x)

        return {"x": x_arr,
                "y": y_arr,
                "gista_y": gista_y,
                "gista_x": gista_x
                }

    def create_plot(self):
        n = float(self.ui.nEdit.text())
        k = float(self.ui.kEdit.text())
        t = float(self.ui.tEdit.text())
        l = float(self.ui.lambdaEdit.text())
        points = self.gen_plots(n, k, t, l)
        bar = pyqtgraph.BarGraphItem(x=points["gista_x"], height=points["gista_y"],
                                     width=t, brush='g')
        self.ui.graphicsView.addItem(bar)
        #self.ui.graphicsView.plot(points["x"], points["y"], pen='b')

    def clear_plot(self):
        self.ui.graphicsView.clear()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

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
        pass

    def create_plot(self):
        n = float(self.ui.nEdit.text())
        m = float(self.ui.mEdit.text())
        ro = float(self.ui.roEdit.text())
        r = float(self.ui.REdit.text())

        if self.ui.radio1.isChecked():
            print(1)
        elif self.ui.radio2.isChecked():
            print(2)
        elif self.ui.radio3.isChecked():
            print(3)

    def clear_plot(self):
        self.ui.graphicsView.clear()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

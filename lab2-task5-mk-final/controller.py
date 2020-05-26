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
        self.ui.graphicsView.addLegend()

    @staticmethod
    def create_random():
        a = -0.01
        b = 0.01
        return a + (b - a) * random.random()

    def gen_plots(self, n, ro, m):
        x_arr = numpy.arange(0, ro, 0.1)
        y_arr = []
        y_exp = []
        sigmas = []
        for x in x_arr:
            if x < 1:
                y_th = x / (1 - x ** (m + 2)) * (1 + x ** (m + 1) * (m * x - m + x - 2)) / (1 - x)
            elif x == 1:
                y_th = ((m + 1) / 2) * x
            else:
                y_th = x / (1 - x ** (m + 2)) * (1 + x ** (m + 1) * (m * x - m + x - 2)) / (1 - x)
            y_arr.append(y_th)

        for y in y_arr:
            rand = self.create_random()
            val = y + rand
            y_exp.append(val)

        return {
            "x": x_arr,
            "y": y_arr,
            "y_exp": y_exp,
            "sigmas": sigmas
        }

    def create_plot(self):
        n = float(self.ui.nEdit.text())
        m = float(self.ui.mEdit.text())
        ro = float(self.ui.roEdit.text())
        r = float(self.ui.REdit.text())

        '''
        n = 5000
        m = 6
        r = 15
        ro = 3'''
        
        points = self.gen_plots(n, ro, m)
        pen_style = pyqtgraph.mkPen('g', width=2)
        self.ui.graphicsView.plot(points["x"], points["y"], pen=pen_style, name="Теория")
        self.ui.graphicsView.plot(points["x"], points["y_exp"], name='Эксперимент', pen=None)
        self.ui.graphicsView.plot(points["x"], points["sigmas"], name='Стандарт.откл', pen=None)        


        '''if self.ui.radio1.isChecked():
            print(1)
        elif self.ui.radio2.isChecked():
            print(2)
        elif self.ui.radio3.isChecked():
            print(3)'''

    def clear_plot(self):
        self.ui.graphicsView.clear()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

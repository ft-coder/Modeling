import pyqtgraph
import random
import sys
import numpy

from PyQt5 import QtWidgets, QtCore
from model import Ui_Form
from math import sqrt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.createButt.clicked.connect(self.create_plot)
        self.ui.clearButt.clicked.connect(self.clear_plot)
        self.ui.graphicsView.addLegend()
        self.ui.graphicsView.setBackground(background='w')
        self.ui.graphicsView.showGrid(x=True, y=True)

    def create_random(self, a, b, n):
        array = []
        for i in range(0, n):
            pair = {}
            x = a + (b - a) * random.random()
            y = 0.235 * random.random()
            pair["x"] = x
            pair["y"] = y
            array.append(pair)
        return array

    @staticmethod
    def func1(x):
        return x / 17

    @staticmethod
    def func2(x):
        return 2 / 51 * (x + 1)

    @staticmethod
    def func3(x):
        return 1 / 51 * (32 - 4 * x)


    def gen_plots(self, a, b, alfa, beta, n):
        x_arr = numpy.arange(a, b, 0.5)
        sigmas = []
        Q_exp = []

        for x in x_arr:
            buff_variation = 0
            buff_q_exp = 0
            nayman_pairs = self.create_random(a, b, n)

            q_th = 0
            if 0 < x < 2:
                q_th = self.func1(x)
            elif 2 < x < 5:
                q_th = self.func2(x)
            elif 5 < x < 8:
                q_th = self.func3(x)

            for pair in nayman_pairs:
                if pair['x'] > pair['y']:
                    q_exp = alfa * (pair['x'] - pair['y'])
                else:
                    q_exp = beta * (pair['y'] - pair['x'])
                buff_variation += (q_th - q_exp) ** 2
                buff_q_exp += q_exp
            '''Sigma'''
            d = buff_variation / (len(nayman_pairs))
            sigma = sqrt(d)
            sigmas.append(sigma)
            '''Exp'''
            Q_exp.append(buff_q_exp / (len(nayman_pairs)))

        return {"q_exp": Q_exp,
                "sigma": sigmas,
                "x_arr": x_arr}

    def create_stats_exp(self, x_array, y_array):
        y = min(y_array)
        y_index = y_array.index(min(y_array))
        x = x_array[y_index]
        self.ui.x_exp_Edit.setText(str(round(x, 2)))
        self.ui.q_exp_Edit.setText(str(round(y, 2)))

    def create_plot(self):
        a = float(self.ui.A_Edit.text())
        b = float(self.ui.B_Edit.text())
        alfa = float(self.ui.alfa_Edit.text())
        beta = float(self.ui.beta_Edit.text())
        n = int(self.ui.n_Edit.text())

        points = self.gen_plots(a, b, alfa, beta, n)

        pen_style = pyqtgraph.mkPen('b', width=2)
        self.ui.graphicsView.plot(points["x_arr"][::20], points["q_exp"][::20], name='Эксперимент', pen=None,
                                  symbol='o')
        self.ui.graphicsView.plot(points["x_arr"],points["q_exp"],pen=pen_style)
        self.create_stats_exp(points["x_arr"], points["q_exp"])

        pen_style = pyqtgraph.mkPen('r', pen_style=QtCore.Qt.DotLine, width=2)
        self.ui.graphicsView.plot(points["x_arr"], points["sigma"], name='Стандарт.откл', pen=pen_style)

    def clear_plot(self):
        self.ui.graphicsView.clear()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

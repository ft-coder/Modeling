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

    @staticmethod
    def create_random(a, b, n):
        rand_arr = []
        for i in range(0, n):
            rand_arr.append(a + (b - a) * random.random())
        return rand_arr

    def gen_plots(self, a, b, alfa, beta, n):
        x_arr = numpy.arange(a, b, 0.01)
        sigmas = []
        Q_th = []
        Q_exp = []

        for x in x_arr:
            buff_variation = 0
            buff_q_exp = 0
            y_array = self.create_random(a, b, n)
            q_th = (1 / ((b - a) * 2)) * ((alfa * (x - a) ** 2) + (beta * (x - b) ** 2))
            for y in y_array:
                if x > y:
                    q_exp = alfa * (x - y)
                else:
                    q_exp = beta * (y - x)
                buff_variation += (q_th - q_exp) ** 2
                buff_q_exp += q_exp
            '''Sigma'''
            d = buff_variation / (len(y_array))
            sigma = sqrt(d)
            sigmas.append(sigma)
            '''Exp'''
            Q_exp.append(buff_q_exp / (len(y_array)))
            '''Th'''
            Q_th.append(q_th)

        return {"q_th": Q_th,
                "q_exp": Q_exp,
                "sigma": sigmas,
                "x_arr": x_arr}

    def create_stats(self, a, b, alfa, beta):
        x = (alfa * a + beta * b) / (alfa + beta)
        y = (1 / ((b - a) * 2)) * ((alfa * (x - a) ** 2) + (beta * (x - b) ** 2))
        self.ui.x_th_Edit.setText(str(round(x, 2)))
        self.ui.q_th_Edit.setText(str(round(y, 2)))

    def create_stats_exp(self, x_array, y_array):
        y = min(y_array)
        y_index = y_array.index(min(y_array))
        x = x_array[y_index]
        self.ui.x_exp_Edit.setText(str(round(x, 2)))
        self.ui.q_exp_Edit.setText(str(round(y, 2)))

    def create_plot(self):
        a = self.ui.A_Edit.text()
        b = self.ui.B_Edit.text()
        alfa = self.ui.alfa_Edit.text()
        beta = self.ui.beta_Edit.text()
        n = self.ui.n_Edit.text()

        points = self.gen_plots(float(a), float(b), float(alfa), float(beta), int(n))

        pen_style = pyqtgraph.mkPen('g', width=3)
        self.ui.graphicsView.plot(points["x_arr"], points["q_th"], name='Теория', pen=pen_style)
        self.create_stats(float(a), float(b), float(alfa), float(beta))

        pen_style = pyqtgraph.mkPen('b', width=2)
        self.ui.graphicsView.plot(points["x_arr"][::20], points["q_exp"][::20], name='Эксперимент', pen=None,
                                  symbol='o')
        # self.ui.graphicsView.plot(points["x_arr"],points["q_exp"],pen=pen_style)
        self.create_stats_exp(points["x_arr"], points["q_exp"])

        pen_style = pyqtgraph.mkPen('r', pen_style=QtCore.Qt.DotLine, width=2)
        self.ui.graphicsView.plot(points["x_arr"], points["sigma"], name='Стандарт.откл', pen=pen_style)

    def clear_plot(self):
        self.ui.graphicsView.clear()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

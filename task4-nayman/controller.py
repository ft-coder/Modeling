import pyqtgraph
import random
import sys

from numpy import arange
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
        self.H = 0

    def create_random(self, a, d):
        x = a + (d - a) * random.random()
        y = self.H * random.random()
        return {
            "x": x,
            "y": y
        }

    @staticmethod
    def find_h(a, b, c, d):
        return 1 / ((c - b) / 4 + (b - a) / 4 + (c - b) / 2 + (d - c) / 2)

    @staticmethod
    def func1(x):
        return x / 17

    @staticmethod
    def func2(x):
        return 2/51 * (x + 1)

    @staticmethod
    def func3(x):
        return 1/51 * (32 - 4 * x)

    def gen_plot(self, a, b, c, d):
        func1_points = {
            "x1": a,
            "y1": self.func1(a),
            "x2": b,
            "y2": self.func1(b)
        }

        func2_points = {
            "x1": b,
            "y1": self.func2(b),
            "x2": c,
            "y2": self.func2(c)
        }

        func3_points = {
            "x1": c,
            "y1": self.func3(c),
            "x2": d,
            "y2": self.func3(d)
        }
        return [func1_points, func2_points, func3_points]

    # https://studfile.net/preview/4662079/page:42/
    def gen_barchart(self, a, b, c, d, n):
        points = []
        for i in range(0, n):
            rand_pair = self.create_random(a, d)
            if a < rand_pair["x"] < b:
                if rand_pair["y"] < self.func1(rand_pair["x"]):
                    points.append(rand_pair)
            elif b < rand_pair["x"] < c:
                if rand_pair["y"] < self.func2(rand_pair["x"]):
                    points.append(rand_pair)
            elif c < rand_pair["x"] < d:
                if rand_pair["y"] < self.func3(rand_pair["x"]):
                    points.append(rand_pair)

        means = {i: [0, 0] for i in arange(a, d, 0.5)}

        for key, value in means.items():
            for point in points:
                if key < point["x"] < key + 0.5:
                    value[0] += point["y"]
                    value[1] += 1

        points = []

        for key, value in means.items():
            points.append({
                "x": key,
                "y": value[0]/value[1]
            })

        return points

    def create_plot(self):
        a = int(self.ui.A_Edit.text())
        b = int(self.ui.B_Edit.text())
        c = int(self.ui.C_Edit.text())
        d = int(self.ui.D_Edit.text())
        n = int(self.ui.n_Edit.text())
        '''a = 0
        b = 2
        c = 5
        d = 8
        n = 5000'''

        self.H = self.find_h(a, b, c, d)
        self.ui.H_Edit.setText(str(round(self.H, 3)))

        bars = self.gen_barchart(a, b, c, d, n)

        barchart = pyqtgraph.BarGraphItem(x0=[bar["x"] for bar in bars],
                                          width=0.5,
                                          height=[bar["y"]*2 for bar in bars],
                                          brush='g')
        self.ui.graphicsView.addItem(barchart)

        points = self.gen_plot(a, b, c, d)
        self.ui.graphicsView.plot(
            (points[0]["x1"], points[0]["x2"]),
            (points[0]["y1"], points[0]["y2"]),
            pen='r'
        )

        self.ui.graphicsView.plot(
            (points[1]["x1"], points[1]["x2"]),
            (points[1]["y1"], points[1]["y2"]),
            pen='r'
        )

        self.ui.graphicsView.plot(
            (points[2]["x1"], points[2]["x2"]),
            (points[2]["y1"], points[2]["y2"]),
            pen='r'
        )

    def clear_plot(self):
        self.ui.graphicsView.clear()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

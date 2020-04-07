import pyqtgraph
import random
import sys
from PyQt5 import QtWidgets, QtCore
from model import Ui_Form


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

    def gen_plots(self, a, b, c, d, n):
        pass

    def create_plot(self):
        a = self.ui.A_Edit.text()
        b = self.ui.B_Edit.text()
        c = self.ui.C_Edit.text()
        d = self.ui.D_Edit.text()
        n = self.ui.n_Edit.text()

    def clear_plot(self):
        self.ui.graphicsView.clear()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

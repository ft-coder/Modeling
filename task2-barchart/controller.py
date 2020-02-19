import pyqtgraph
import sys
import os

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
        self.ui.graphicsView.showGrid(x = True, y = True)

     def create_plot():
        pass
     def clear_plot():
        pass
app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
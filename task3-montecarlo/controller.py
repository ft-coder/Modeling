import pyqtgraph
import random
import sys
import os

from PyQt5 import QtWidgets, QtCore
from model import Ui_Form
from collections import Counter

class MainWindow(QtWidgets.QMainWindow):
     def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.createButt.clicked.connect(self.create_plot)
        self.ui.clearButt.clicked.connect(self.clear_plot)
        self.ui.graphicsView.addLegend()
        self.ui.graphicsView.showGrid(x = True, y = True)

     def createRandom(self):
        rand_arr = []
        for i in range(0,1000):
            rand_arr.append(random.randint(int(A),int(B)))
        return rand_arr

     def createTheory(self,A,B,alfa,beta):
        Q = []
        for x in range(0,1000):
            q = ( 1/(B-A) )*( (alfa*(x-A)**2)/2 + (beta * (x-B)**2)/2 )
            Q.append(q)
        return Q
     
     def createExp(self,A,B,alfa,beta):
        y_array = self.createRandom()
        Q = []

        pass
        

     def createVariation(self):
         pass
        
     def create_plot(self):
         A = self.ui.A_Edit.text()
         B = self.ui.B_Edit.text()
         alfa = self.ui.alfa_Edit.text()
         beta = self.ui.beta_Edit.text()
        
     def clear_plot(self):
        self.ui.graphicsView.clear()

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
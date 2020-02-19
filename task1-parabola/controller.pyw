import pyqtgraph
import sys
import os

from PyQt5 import QtWidgets, QtCore
from model import Ui_Form



#pyuic5 view.ui -o model.py
#pip install pyqtgraph
#http://www.pyqtgraph.org/documentation/functions.html#color-pen-and-brush-functions

graph_counter = 0

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.createButt.clicked.connect(self.create_plot)
        self.ui.clearButt.clicked.connect(self.clear_plot)
        self.ui.graphicsView.addLegend()
        #self.ui.graphicsView.setConfigOptions(crashWarning=True)
        self.ui.graphicsView.showGrid(x = True, y = True)
      

        
    def create_parabola(self,a,b,c):
        
        x = [point for point in range(-100,100)] 
        y = []

        for point in x:
            y.append(float(a)*(point**2) + float(b)*point + float(c))

        return (x,y)

    def create_func_name(self,a,b,c):
        line = a + "x^2"
        
        if b[0] == "-":
            line+=b + "x"
        else:
            line+="+" + b + "x"

        if c[0] == "-":
            line+=c
        else:
            line+="+" + c
        
        return line

    def input_validation(self,a,b,c):
        try:
            buff = float(a)
            buff = float(b)
            buff = float(c)
        except ValueError:
            return False

        return True

    def create_plot(self):
        a = self.ui.A_Edit.text()
        b = self.ui.B_Edit.text()
        c= self.ui.C_Edit.text()

        if self.input_validation(a,b,c) == False:
            QtWidgets.QMessageBox.about(self, "Упс", "Попробуйте снова.")
            return

        global graph_counter
        graph_colors = ["r", "g", "b", "c", "m", "y", "k", "w"]

        points = self.create_parabola(a,b,c)
        
        if graph_counter < 7:
            self.ui.graphicsView.plot(points[0],points[1],name=self.create_func_name(a,b,c), pen=graph_colors[graph_counter])
        else:
            graph_counter = 0
            self.ui.graphicsView.plot(points[0],points[1],name=self.create_func_name(a,b,c), pen=graph_colors[graph_counter])
        graph_counter += 1
        
        
    def clear_plot(self):
        self.ui.graphicsView.clear()
        graph_counter = 0
        #self.ui.graphicsView.removeItem(legend)
        
       

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
import pyqtgraph
import random
import sys
import os
import numpy


from PyQt5 import QtWidgets, QtCore
from model import Ui_Form
from collections import Counter
from math import sqrt, pow


class MainWindow(QtWidgets.QMainWindow):
     def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.createButt.clicked.connect(self.create_plot)
        self.ui.clearButt.clicked.connect(self.clear_plot)
        self.ui.graphicsView.addLegend()
        self.ui.graphicsView.setBackground(background='w')
        self.ui.graphicsView.showGrid(x = True, y = True)

        self.Q_th = []
        self.Q_exp = []

     def createRandom(self,A,B,n):
        return numpy.random.randint(A,B, n)

     def createTheory(self,A,B,alfa,beta):
        Q = [[],[]]
        x = A
        while x < B:
            y = ( 1/((B-A)*2) )*( (alfa*(x-A)**2) + (beta * (x-B)**2) )
            self.Q_th.append(y)
            Q[0].append(y)
            Q[1].append(x)
            x += 0.01
        return Q
     

     def createExp(self,A,B,alfa,beta,n):
        x_arr = numpy.arange(A, B, 0.01)
        Q = []
        for x in x_arr:
            buff = 0
            y_array = self.createRandom(A,B,n)
            for y in y_array:
                if  x > y:
                    q = alfa * (x-y)
                else:
                    q = beta * (y-x)
                buff += q
            self.Q_exp.append( buff/len(y_array))
            Q.append( buff/len(y_array))
        return [Q, x_arr]

            

     def createVariation(self,A,B, alfa, beta,n):
         x_arr = numpy.arange(A, B, 0.01)
         sigmas = []
         for x in x_arr:
            buff = 0
            y_array = self.createRandom(A,B,n)
            q_th = ( 1/((B-A)*2) )*( (alfa*(x-A)**2) + (beta * (x-B)**2) )
            for y in y_array:
                if  x > y:
                    q_exp = alfa * (x-y)
                else:
                    q_exp = beta * (y-x)
                buff += (q_th - q_exp)**2
            d = buff/len(y_array)
            sigma = sqrt(d)
            sigmas.append(sigma)
         return [sigmas, x_arr]
         

     def createStats(self,A,B,alfa,beta):
         x = ( alfa*A + beta*B ) / ( alfa+beta )
         y = ( 1/((B-A)*2) )*( (alfa*(x-A)**2) + (beta * (x-B)**2) )
         #self.ui.stats.setText("Теория:\nQ(x*) = " + str(round(y,2)) + "\nx* = " + str(round(x,2)))
         self.ui.x_th_Edit.setText(str(round(x,2)))
         self.ui.q_th_Edit.setText(str(round(y,2)))

     def createStatsExp(self,x_array, y_array):
         y = min(y_array)
         y_index = y_array.index(min(y_array))
         x = x_array[y_index]
         #self.ui.stats.setText( self.ui.stats.text() + "\nЭксперимент:\nQ(x*) = " + str(round(y,2)) + "\nx* = " + str(round(x,2)) )
         self.ui.x_exp_Edit.setText(str(round(x,2)))
         self.ui.q_exp_Edit.setText(str(round(y,2)))
       
     def create_plot(self):
         A = self.ui.A_Edit.text()
         B = self.ui.B_Edit.text()
         alfa = self.ui.alfa_Edit.text()
         beta = self.ui.beta_Edit.text()
         n = self.ui.n_Edit.text()
         
         points = self.createTheory(float(A),float(B),float(alfa),float(beta))
         pen_style = pyqtgraph.mkPen('g', width=3)
         self.ui.graphicsView.plot(points[1],points[0],name='Теория',pen=pen_style)
         self.createStats(float(A),float(B),float(alfa),float(beta))
         

         points = self.createExp(float(A),float(B),float(alfa),float(beta), int(n))
         pen_style = pyqtgraph.mkPen('b', width=2)
         self.ui.graphicsView.plot(points[1][0::40], points[0][0::40],name='Эксперимент', pen=None, symbol= 'o')
         #self.ui.graphicsView.plot(points[1][0::40],points[0][0::40],pen=pen_style)
         self.createStatsExp(points[1], points[0])

        
         points = self.createVariation(float(A),float(B),float(alfa),float(beta),int(n))
         pen_style = pyqtgraph.mkPen('r', pen_style=QtCore.Qt.DotLine, width=2)
         self.ui.graphicsView.plot(points[1][0::40], points[0][0::40], name='Стандарт.откл',pen=pen_style)

         self.Q_exp=[]
         self.Q_th=[]

     def clear_plot(self):
        self.ui.graphicsView.clear()

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
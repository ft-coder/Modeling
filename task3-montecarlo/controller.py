import pyqtgraph
import random
import sys
import os

from PyQt5 import QtWidgets, QtCore
from model import Ui_Form
from collections import Counter
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
        self.ui.graphicsView.showGrid(x = True, y = True)

        self.Q_th = []
        self.Q_exp = []


        

     def createRandom(self,A,B):
        rand_arr = []
        for i in range(0,500):
            rand_arr.append(random.randint(int(A),int(B)))
        return rand_arr

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
     

     def createExp(self,A,B,alfa,beta):
        y_array = self.createRandom(A,B)
        Q = [[],[]]

        x = A
        while x < B:
            buff = 0
            for y in y_array:
                if  x > y:
                    q = alfa * (x-y)
                else:
                    q = beta * (y-x)
                buff += q
            self.Q_exp.append(buff/len(y_array))
            Q[0].append(buff/len(y_array))
            Q[1].append(x)
            x += 0.01
        return Q    


     def createVariation(self, x_array):
         X_Y = [[],[]]
         
         for q_th, q_exp in dict(zip(self.Q_th, self.Q_exp)).items():
             sigma = sqrt( (q_th - q_exp)**2)
             print(sigma)
             X_Y[0].append(sigma)
         X_Y[1] = x_array[0:-2:1]
            
         return X_Y        
         

              
        
     def create_plot(self):
         #A = self.ui.A_Edit.text()
         #B = self.ui.B_Edit.text()
         #alfa = self.ui.alfa_Edit.text()
         #beta = self.ui.beta_Edit.text()
         A=0
         B=10
         alfa=1
         beta=1
         
         points = self.createTheory(float(A),float(B),float(alfa),float(beta))
         self.ui.graphicsView.plot(points[1],points[0],name='Теория',pen='g')
         

         points = self.createExp(float(A),float(B),float(alfa),float(beta))
         self.ui.graphicsView.plot(points[1], points[0],name='Эксперимент', pen='r')
        
         points = self.createVariation(points[1])
         self.ui.graphicsView.plot(points[1], points[0], name='Ср.квадрат.откл',pen='b')

         self.Q_exp=[]
         self.Q_th=[]

     def clear_plot(self):
        self.ui.graphicsView.clear()

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
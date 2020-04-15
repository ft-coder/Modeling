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
        self.ui.graphicsView.setBackground(background='w')
        self.ui.graphicsView.showGrid(x = True, y = True)
 
     def random_array(self,N,A,B):
         rand_arr = []
         for i in range(0, int(N)):
             rand_arr.append(int((int(A) + (int(B) - int(A)) * random.random())))
         return rand_arr



     def input_validation(self,a,b,n,N):
        try:
            buff = float(a)
            buff = float(b)
            buff = float(n)
            buff = float(N)
            for i in (float(n),float(N)):
                if i < 0:
                    return False
        except ValueError:
            return False
        return True

    # Divides one random array to dict of intervals and values
     def create_groups(self,n, random_arr, A, B):
         c = Counter(random_arr)
         interval_len = len(range(A,B))/n
         print("Интервал:" + str(interval_len))

         d = {}

         i = A
         j = A + interval_len 

         while j <= B:
            print(i,j)
            if j not in d:
                 d[j] = 0

            for key,value in c.items():
                if key >= i and key <= j:
                    d[j] += value

            i = j
            j += interval_len
             

         return (d,interval_len)
            
     def calc_probability(self,array,N):
         for val in array[0].values():
             val = val / N
         return array

     def create_plot(self):
         A = self.ui.A_Edit.text()
         B = self.ui.B_Edit.text()
         n = self.ui.n_Edit.text()
         N = self.ui.N_Edit.text()

         # Input validation
         if self.input_validation(A,B,n,N) == False:
            QtWidgets.QMessageBox.about(self, "Упс", "Попробуйте снова.")
            return
         
         # Creating array of ints
         rand_arr = self.random_array(N,A,B)
         print(rand_arr)

         #Counts repeatings of each number in array and divides to intervals
         intervals_counts = self.create_groups(int(n), rand_arr, int(A), int(B))
         print(intervals_counts)

         #intervals_counts = self.calc_probability(intervals_counts,int(N))
         #print(intervals_counts)

         #for key,value in intervals_counts[0].items():
         bar = pyqtgraph.BarGraphItem(x0=range(int(A),int(B),int(intervals_counts[1])),
                                      width=intervals_counts[1],
                                      height=[float(val)/float(N) for val in intervals_counts[0].values()] ,
                                      brush='g')
         self.ui.graphicsView.addItem(bar)
         '''bar = pyqtgraph.BarGraphItem(x0 = range(0,30,10),width=10,height=[24,25,10], brush='g')
         self.ui.graphicsView.addItem(bar)'''
        
     def clear_plot(self):
        self.ui.graphicsView.clear()

app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(846, 678)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(846, 678))
        self.graphicsView = PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(205, 11, 621, 651))
        self.graphicsView.setObjectName("graphicsView")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 171, 211))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(21, 21, 171, 138))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.N_Edit = QtWidgets.QLineEdit(self.widget)
        self.N_Edit.setObjectName("N_Edit")
        self.horizontalLayout_2.addWidget(self.N_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.n_Edit = QtWidgets.QLineEdit(self.widget)
        self.n_Edit.setObjectName("n_Edit")
        self.horizontalLayout_3.addWidget(self.n_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.A_Edit = QtWidgets.QLineEdit(self.widget)
        self.A_Edit.setObjectName("A_Edit")
        self.horizontalLayout_4.addWidget(self.A_Edit)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.B_Edit = QtWidgets.QLineEdit(self.widget)
        self.B_Edit.setObjectName("B_Edit")
        self.horizontalLayout_4.addWidget(self.B_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.createButt = QtWidgets.QPushButton(self.widget)
        self.createButt.setObjectName("createButt")
        self.verticalLayout.addWidget(self.createButt)
        self.clearButt = QtWidgets.QPushButton(self.widget)
        self.clearButt.setAutoDefault(False)
        self.clearButt.setDefault(False)
        self.clearButt.setObjectName("clearButt")
        self.verticalLayout.addWidget(self.clearButt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">N - количество сгенерированных случайных чисел</span></p><p><span style=\" font-size:11pt;\">n - количество столбцов</span></p><p><span style=\" font-size:11pt;\">А и B - интервал, в котором задаются случайные числа</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "N:"))
        self.label_3.setText(_translate("Form", "n: "))
        self.label_5.setText(_translate("Form", "A:"))
        self.label_6.setText(_translate("Form", "B:"))
        self.createButt.setText(_translate("Form", "Построить график"))
        self.clearButt.setText(_translate("Form", "Очистить координатную сетку"))
from pyqtgraph import PlotWidget

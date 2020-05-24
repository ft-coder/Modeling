# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(773, 610)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(846, 678))
        self.graphicsView = PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(160, 10, 601, 591))
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 21, 141, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.aEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.aEdit.setObjectName("aEdit")
        self.verticalLayout.addWidget(self.aEdit)
        self.label1 = QtWidgets.QLabel(self.layoutWidget)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.bEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.bEdit.setObjectName("bEdit")
        self.verticalLayout.addWidget(self.bEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.intervals = QtWidgets.QLineEdit(self.layoutWidget)
        self.intervals.setObjectName("intervals")
        self.verticalLayout.addWidget(self.intervals)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.numbers = QtWidgets.QLineEdit(self.layoutWidget)
        self.numbers.setObjectName("numbers")
        self.verticalLayout.addWidget(self.numbers)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lambdaEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lambdaEdit.setObjectName("lambdaEdit")
        self.verticalLayout.addWidget(self.lambdaEdit)
        self.createButt = QtWidgets.QPushButton(self.layoutWidget)
        self.createButt.setObjectName("createButt")
        self.verticalLayout.addWidget(self.createButt)
        self.clearButt = QtWidgets.QPushButton(self.layoutWidget)
        self.clearButt.setAutoDefault(False)
        self.clearButt.setDefault(False)
        self.clearButt.setObjectName("clearButt")
        self.verticalLayout.addWidget(self.clearButt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Журавлев"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">А:</p></body></html>"))
        self.label1.setText(_translate("Form", "<html><head/><body><p align=\"center\">В:</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">Количество </p><p align=\"center\">cтолбцов:</p></body></html>"))
        self.label_4.setText(_translate("Form", "Количество чисел:"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">Lambda:</p></body></html>"))
        self.createButt.setText(_translate("Form", "Построить \n"
"график"))
        self.clearButt.setText(_translate("Form", "Очистить"))
from pyqtgraph import PlotWidget

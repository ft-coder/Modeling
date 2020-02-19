# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


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
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 176, 138))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.A_Edit = QtWidgets.QLineEdit(self.widget)
        self.A_Edit.setObjectName("A_Edit")
        self.horizontalLayout_2.addWidget(self.A_Edit)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.B_Edit = QtWidgets.QLineEdit(self.widget)
        self.B_Edit.setObjectName("B_Edit")
        self.horizontalLayout_3.addWidget(self.B_Edit)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.C_Edit = QtWidgets.QLineEdit(self.widget)
        self.C_Edit.setObjectName("C_Edit")
        self.horizontalLayout.addWidget(self.C_Edit)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.createButt = QtWidgets.QPushButton(self.widget)
        self.createButt.setObjectName("createButt")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.createButt)
        self.clearButt = QtWidgets.QPushButton(self.widget)
        self.clearButt.setAutoDefault(False)
        self.clearButt.setDefault(False)
        self.clearButt.setObjectName("clearButt")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.clearButt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "A:"))
        self.label_3.setText(_translate("Form", "B: "))
        self.label.setText(_translate("Form", "C:"))
        self.createButt.setText(_translate("Form", "Построить график"))
        self.clearButt.setText(_translate("Form", "Очистить координатную сетку"))
#from pyqtgraph import PlotWidget

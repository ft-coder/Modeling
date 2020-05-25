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
        self.layoutWidget.setGeometry(QtCore.QRect(8, 21, 141, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lambdaEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lambdaEdit.setObjectName("lambdaEdit")
        self.horizontalLayout.addWidget(self.lambdaEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.tEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.tEdit.setObjectName("tEdit")
        self.horizontalLayout_4.addWidget(self.tEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.kEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.kEdit.setObjectName("kEdit")
        self.horizontalLayout_2.addWidget(self.kEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.nEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.nEdit.setObjectName("nEdit")
        self.horizontalLayout_3.addWidget(self.nEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.label.setText(_translate("Form", "λ:  "))
        self.label_4.setText(_translate("Form", "ΔТ:"))
        self.label_2.setText(_translate("Form", "k:  "))
        self.label_3.setText(_translate("Form", "n: "))
        self.createButt.setText(_translate("Form", "Построить \n"
"график"))
        self.clearButt.setText(_translate("Form", "Очистить"))
from pyqtgraph import PlotWidget

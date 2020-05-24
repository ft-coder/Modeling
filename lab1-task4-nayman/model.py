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
        Form.resize(813, 654)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(846, 678))
        Form.setWindowTitle("")
        self.graphicsView = PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(130, 20, 671, 621))
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 21, 111, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.A_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.A_Edit.setObjectName("A_Edit")
        self.horizontalLayout.addWidget(self.A_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.B_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.B_Edit.setObjectName("B_Edit")
        self.horizontalLayout_2.addWidget(self.B_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.C_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.C_Edit.setObjectName("C_Edit")
        self.horizontalLayout_3.addWidget(self.C_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.D_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.D_Edit.setObjectName("D_Edit")
        self.horizontalLayout_4.addWidget(self.D_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.n_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.n_Edit.setObjectName("n_Edit")
        self.horizontalLayout_5.addWidget(self.n_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.createButt = QtWidgets.QPushButton(self.layoutWidget)
        self.createButt.setObjectName("createButt")
        self.verticalLayout.addWidget(self.createButt)
        self.clearButt = QtWidgets.QPushButton(self.layoutWidget)
        self.clearButt.setAutoDefault(False)
        self.clearButt.setDefault(False)
        self.clearButt.setObjectName("clearButt")
        self.verticalLayout.addWidget(self.clearButt)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.H_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.H_Edit.setObjectName("H_Edit")
        self.horizontalLayout_8.addWidget(self.H_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "A:"))
        self.label_2.setText(_translate("Form", "B:"))
        self.label_3.setText(_translate("Form", "C:"))
        self.label_4.setText(_translate("Form", "D:"))
        self.label_5.setText(_translate("Form", "n:"))
        self.createButt.setText(_translate("Form", "Построить \n"
"график"))
        self.clearButt.setText(_translate("Form", "Очистить \n"
"координатную \n"
"сетку"))
        self.label_9.setText(_translate("Form", "H:"))
from pyqtgraph import PlotWidget

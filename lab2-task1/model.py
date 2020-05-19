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
        Form.resize(773, 610)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(846, 678))
        self.graphicsView = PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(150, 10, 611, 591))
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 21, 131, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.p_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.p_Edit.setObjectName("p_Edit")
        self.horizontalLayout_2.addWidget(self.p_Edit)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.m_Edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.m_Edit.setObjectName("m_Edit")
        self.horizontalLayout_2.addWidget(self.m_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
        self.label_2.setText(_translate("Form", "p="))
        self.label.setText(_translate("Form", "m="))
        self.createButt.setText(_translate("Form", "Построить \n"
"график"))
        self.clearButt.setText(_translate("Form", "Очистить"))
from pyqtgraph import PlotWidget

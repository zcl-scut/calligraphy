# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import picture_rc

class Ui_Register(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 407)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 140, 231, 31))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(150, 240, 231, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 150, 31, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 240, 71, 21))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(160, 30, 221, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 350, 231, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 290, 51, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 290, 51, 31))
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(150, 60, 231, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 60, 31, 21))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(150, 190, 231, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 200, 31, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 110, 31, 21))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(290, 110, 41, 18))
        self.radioButton_1 = QRadioButton(self.centralwidget)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setGeometry(QRect(200, 110, 41, 18))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u5728\u7ebf\u5b66\u4e60\u5206\u6790\u7cfb\u7edf\u5b66\u751f\u7aef", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u534e\u5357\u7406\u5de5\u5927\u5b66\u7248\u6743\u6240\u6709@scut.edu.cn", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5973", None))
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow", u"\u7537", None))
    # retranslateUi


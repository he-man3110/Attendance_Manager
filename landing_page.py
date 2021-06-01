# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'landing_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/DEV/Python/PyQT/AM/res/logoo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame{\n"
"background : black;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QLabel{\n"
"background: transparent;\n"
"color: white;\n"
"} \n"
"\n"
"QPushButton{\n"
"color: transparent;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#close_button:hover {\n"
"background: red;\n"
"color: black;\n"
"border: 4px red solid;\n"
"}\n"
"\n"
"QPushButton#minimize_button:hover {\n"
"background: red;\n"
"color: black;\n"
"border: 4px red solid;\n"
"}\n"
"\n"
"QPushButton#drop_button:hover {\n"
"background: red;\n"
"color: black;\n"
"border: 4px red solid;\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 1061, 701))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QPushButton#sign_up_button, QPushButton#sign_in_button{\n"
"color: grey;\n"
"background: #222;\n"
"border-radius: 24px;\n"
"border-top: 5px solid black;\n"
"border-bottom: 5px solid black;\n"
"border-left: 5px solid black;\n"
"border-right: 5px solid black;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton#sign_up_button:hover{\n"
"border-top: 3px solid rgb(28, 235, 13);\n"
"border-bottom: 3px solid rgb(28, 235, 13);\n"
"border-left: 3px solid rgb(28, 235, 13);\n"
"border-right: 3px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton#sign_in_button:hover{\n"
"border-top: 3px solid rgb(28, 235, 13);\n"
"border-bottom: 3px solid rgb(28, 235, 13);\n"
"border-left: 3px solid rgb(28, 235, 13);\n"
"border-right: 3px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton#sign_in_button:pressed{\n"
"margin-top: 3px solid white;\n"
"margin-bottom: 3px solid white;\n"
"margin-left: 3px solid white;\n"
"margin-right: 3px solid white;\n"
"}\n"
"\n"
"QPushButton#sign_up_button:pressed{\n"
"margin-top: 3px solid white;\n"
"margin-bottom: 3px solid white;\n"
"margin-left: 3px solid white;\n"
"margin-right: 3px solid white;\n"
"}\n"
"\n"
"QPushButton#set_config{\n"
"background : url(D:/DEV/Python/PyQT/AM/res/settings_gear_white.svg) no-repeat center center fixed;\n"
"}\n"
"\n"
"QPushButton#set_config:hover {\n"
"background : url(D:/DEV/Python/PyQT/AM/res/settings_gear_green_hover.svg) no-repeat center center fixed;\n"
"}\n"
"\n"
"QPushButton#set_config:pressed {\n"
"background : url(D:/DEV/Python/PyQT/AM/res/settings_gear_dark_green.svg) no-repeat center center fixed;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.top_bar = QtWidgets.QFrame(self.frame)
        self.top_bar.setGeometry(QtCore.QRect(0, 0, 1061, 41))
        self.top_bar.setStyleSheet("background: #222;")
        self.top_bar.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_bar.setObjectName("top_bar")
        self.close_button = QtWidgets.QPushButton(self.frame)
        self.close_button.setGeometry(QtCore.QRect(1021, 11, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("background-color: crimson;\n"
"padding-bottom: 4px;")
        self.close_button.setObjectName("close_button")
        self.minimize_button = QtWidgets.QPushButton(self.frame)
        self.minimize_button.setGeometry(QtCore.QRect(988, 11, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.minimize_button.setFont(font)
        self.minimize_button.setStyleSheet("border-radius: 10px; \n"
"background-color: rgb(252, 213, 13);\n"
"padding-bottom: 4px;")
        self.minimize_button.setObjectName("minimize_button")
        self.drop_button = QtWidgets.QPushButton(self.frame)
        self.drop_button.setGeometry(QtCore.QRect(954, 11, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.drop_button.setFont(font)
        self.drop_button.setStyleSheet("border-radius: 10px; \n"
"background-color: rgb(84, 206, 28);\n"
"padding-bottom: 4px;\n"
"")
        self.drop_button.setObjectName("drop_button")
        self.AM_main_label = QtWidgets.QLabel(self.frame)
        self.AM_main_label.setGeometry(QtCore.QRect(320, 40, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AM_main_label.setFont(font)
        self.AM_main_label.setStyleSheet("color: white;")
        self.AM_main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.AM_main_label.setObjectName("AM_main_label")
        self.__credits__ = QtWidgets.QLabel(self.frame)
        self.__credits__.setGeometry(QtCore.QRect(420, 660, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.__credits__.setFont(font)
        self.__credits__.setAlignment(QtCore.Qt.AlignCenter)
        self.__credits__.setObjectName("__credits__")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(475, 120, 101, 91))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("D:/DEV/Python/PyQT/AM/res/human-resources.svg"))
        self.Logo.setObjectName("Logo")
        self.sign_up_button = QtWidgets.QPushButton(self.frame)
        self.sign_up_button.setGeometry(QtCore.QRect(360, 290, 141, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setStyleSheet("padding-left: 0px;")
        self.sign_up_button.setObjectName("sign_up_button")
        self.sign_in_button = QtWidgets.QPushButton(self.frame)
        self.sign_in_button.setGeometry(QtCore.QRect(570, 290, 141, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_in_button.sizePolicy().hasHeightForWidth())
        self.sign_in_button.setSizePolicy(sizePolicy)
        self.sign_in_button.setMinimumSize(QtCore.QSize(131, 131))
        self.sign_in_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sign_in_button.setFont(font)
        self.sign_in_button.setStyleSheet("padding-left: 0px;")
        self.sign_in_button.setObjectName("sign_in_button")
        self.set_config = QtWidgets.QPushButton(self.frame)
        self.set_config.setGeometry(QtCore.QRect(979, 628, 71, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_config.sizePolicy().hasHeightForWidth())
        self.set_config.setSizePolicy(sizePolicy)
        self.set_config.setStyleSheet("")
        self.set_config.setText("")
        self.set_config.setObjectName("set_config")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(30, 480, 1001, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.error_out.setFont(font)
        self.error_out.setStyleSheet("color: crimson;")
        self.error_out.setText("")
        self.error_out.setAlignment(QtCore.Qt.AlignCenter)
        self.error_out.setObjectName("error_out")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setErrorContextColor(self, color):
            self.error_out.setStyleSheet(f"color : {color};")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Manager"))
        self.close_button.setText(_translate("MainWindow", "x"))
        self.minimize_button.setText(_translate("MainWindow", "-"))
        self.drop_button.setText(_translate("MainWindow", "o"))
        self.AM_main_label.setText(_translate("MainWindow", "ATTENDANCE MANAGER"))
        self.__credits__.setText(_translate("MainWindow", "MADE BY H E M A N ⚡"))
        self.sign_up_button.setText(_translate("MainWindow", "SIGN UP"))
        self.sign_in_button.setText(_translate("MainWindow", "SIGN IN"))

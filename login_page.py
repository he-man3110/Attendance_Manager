# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
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
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QLineEdit{\n"
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
"QLineEdit:hover{\n"
"border-top: 5px solid #222;\n"
"border-bottom: 3px solid rgb(28, 235, 13);\n"
"border-left: 5px solid #222;\n"
"border-right: 5px solid #222;\n"
"}\n"
"\n"
"\n"
"QPushButton#login_button,QPushButton#back_button{\n"
"font-size: 12px;\n"
"background: rgb(28, 235, 13);\n"
"border-radius: 20px;\n"
"color: black;\n"
"border-top: 5px solid black;\n"
"border-bottom: 5px solid black;\n"
"border-left: 5px solid black;\n"
"border-right: 5px solid black;\n"
"}\n"
"\n"
"QPushButton#login_button:hover,QPushButton#back_button:hover{\n"
"font-size: 16px;\n"
"border-top: 5px solid rgb(28, 235, 13);\n"
"border-bottom: 5px solid rgb(28, 235, 13);\n"
"border-left: 5px solid rgb(28, 235, 13);\n"
"border-right: 5px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton#login_button:pressed,QPushButton#back_button:pressed{\n"
"font-size: 12px;\n"
"background-color: rgb(32, 177, 16);\n"
"border-top: 5px solid black;\n"
"border-bottom: 5px solid black;\n"
"border-left: 5px solid black;\n"
"border-right: 5px solid black;\n"
"}\n"
"")
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
        self.login_label = QtWidgets.QLabel(self.frame)
        self.login_label.setGeometry(QtCore.QRect(460, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.username_LE = QtWidgets.QLineEdit(self.frame)
        self.username_LE.setGeometry(QtCore.QRect(350, 260, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_LE.setFont(font)
        self.username_LE.setObjectName("username_LE")
        self.password_LE = QtWidgets.QLineEdit(self.frame)
        self.password_LE.setGeometry(QtCore.QRect(350, 360, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_LE.setFont(font)
        self.password_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_LE.setObjectName("password_LE")
        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(390, 500, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("")
        self.login_button.setObjectName("login_button")
        self.back_button = QtWidgets.QPushButton(self.frame)
        self.back_button.setGeometry(QtCore.QRect(550, 500, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("")
        self.back_button.setObjectName("back_button")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(475, 120, 101, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Dev/Python/PyQT/AM/res/human-resources.svg"))
        self.label.setObjectName("label")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(290, 440, 471, 51))
        self.error_out.setAlignment(QtCore.Qt.AlignHCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.error_out.setFont(font)
        self.error_out.setStyleSheet("color: crimson;")
        self.error_out.setText("")
        self.error_out.setObjectName("error_out")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.close_button.setText(_translate("MainWindow", "x"))
        self.minimize_button.setText(_translate("MainWindow", "-"))
        self.drop_button.setText(_translate("MainWindow", "o"))
        self.AM_main_label.setText(_translate("MainWindow", "ATTENDANCE MANAGER"))
        self.login_label.setText(_translate("MainWindow", "LOGIN"))
        self.username_LE.setPlaceholderText(_translate("MainWindow", "EMAIL"))
        self.password_LE.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.login_button.setText(_translate("MainWindow", "LOGIN"))
        self.back_button.setText(_translate("MainWindow", "BACK"))

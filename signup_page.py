# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_page.ui'
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
"QPushButton#signup_button,QPushButton#back_button{\n"
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
"QPushButton#signup_button:hover,QPushButton#back_button:hover{\n"
"font-size: 16px;\n"
"border-top: 5px solid rgb(28, 235, 13);\n"
"border-bottom: 5px solid rgb(28, 235, 13);\n"
"border-left: 5px solid rgb(28, 235, 13);\n"
"border-right: 5px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton#signup_button:pressed,QPushButton#back_button:pressed{\n"
"font-size: 12px;\n"
"background-color: rgb(32, 177, 16);\n"
"border-top: 5px solid black;\n"
"border-bottom: 5px solid black;\n"
"border-left: 5px solid black;\n"
"border-right: 5px solid black;\n"
"}\n"
"\n"
"/*\n"
"QComboBox{\n"
"color: white;\n"
"background: black;\n"
"border-radius: 10px;\n"
"border-top: 3px solid green;\n"
"border-bottom: 3px solid green;\n"
"}\n"
"*/\n"
"\n"
"QComboBox {\n"
"    border: 5px solid rgb(28, 235, 13);\n"
"    border-radius: 20px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background: #222;\n"
"    color: white;\n"
"    border-color: black;\n"
"    padding-left: 20px;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: black;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"border-bottom: 5px solid #222;\n"
"border-top: 5px solid #222;\n"
"border-left: 5px solid #222;\n"
"border-right: 5px solid 3222;\n"
"}\n"
"\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: purple;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 35px;\n"
"    border-top: 2px dotted rgb(28, 235, 13);\n"
"    border-left-width: 2px;\n"
"    border-left-color: rgb(28, 235, 13);\n"
"    border-left-style: dotted;\n"
"    border-top-left-radius: 20px; \n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    border-right: 5px solid green;\n"
"    border-bottom: 2px dotted rgb(28, 235, 13);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 35px;\n"
"    border-top: 2px dotted rgb(28, 235, 13);\n"
"    border-left-width: 2px;\n"
"    border-left-color: rgb(28, 235, 13);\n"
"    border-left-style: dotted;\n"
"    border-top-left-radius: 20px; \n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    border-right: 5px solid rgb(28, 235, 13);\n"
"    border-bottom: 2px dotted rgb(28, 235, 13);\n"
"}\n"
"\n"
"QCheckBox{\n"
"background: black;\n"
"color: white;\n"
"spacing: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"    background: #222;\n"
"    border: 3px solid black;\n"
"    border-radius: 10px;\n"
"    /*image : url(\"D:/Dev/Python/PyQT/AM/res/check_mark_2.png\");*/\n"
"}\n"
"\n"
"QCheckBox::indicator:hover{\n"
"border: 3px solid #222;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    border: 3px solid black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(\"D:/Dev/Python/PyQT/AM/res/black_check.svg\");\n"
"    background: rgb(25, 235, 13);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 3px solid rgb(25, 235, 13);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    background: #222;\n"
"    border: 3px solid black;\n"
"}\n"
"\n"
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
        self.login_label.setGeometry(QtCore.QRect(40, 220, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.FirstName_LE = QtWidgets.QLineEdit(self.frame)
        self.FirstName_LE.setGeometry(QtCore.QRect(50, 280, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FirstName_LE.setFont(font)
        self.FirstName_LE.setObjectName("FirstName_LE")
        self.Password_LE = QtWidgets.QLineEdit(self.frame)
        self.Password_LE.setGeometry(QtCore.QRect(50, 440, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password_LE.setFont(font)
        self.Password_LE.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.Password_LE.setObjectName("Password_LE")
        self.signup_button = QtWidgets.QPushButton(self.frame)
        self.signup_button.setGeometry(QtCore.QRect(320, 630, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("")
        self.signup_button.setObjectName("signup_button")
        self.LastName_LE = QtWidgets.QLineEdit(self.frame)
        self.LastName_LE.setGeometry(QtCore.QRect(460, 280, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LastName_LE.setFont(font)
        self.LastName_LE.setObjectName("LastName_LE")
        self.Email_LE = QtWidgets.QLineEdit(self.frame)
        self.Email_LE.setGeometry(QtCore.QRect(50, 360, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Email_LE.setFont(font)
        self.Email_LE.setObjectName("Email_LE")
        self.cpassword_LE = QtWidgets.QLineEdit(self.frame)
        self.cpassword_LE.setGeometry(QtCore.QRect(50, 520, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cpassword_LE.setFont(font)
        self.cpassword_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpassword_LE.setObjectName("cpassword_LE")
        self.Phone_LE = QtWidgets.QLineEdit(self.frame)
        self.Phone_LE.setGeometry(QtCore.QRect(460, 360, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Phone_LE.setFont(font)
        self.Phone_LE.setObjectName("Phone_LE")
        self.bmonth_comboBox = QtWidgets.QComboBox(self.frame)
        self.bmonth_comboBox.setGeometry(QtCore.QRect(620, 440, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bmonth_comboBox.setFont(font)
        self.bmonth_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.bmonth_comboBox.setObjectName("bmonth_comboBox")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bmonth_comboBox.addItem("")
        self.bday_comboBox = QtWidgets.QComboBox(self.frame)
        self.bday_comboBox.setGeometry(QtCore.QRect(470, 440, 144, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bday_comboBox.sizePolicy().hasHeightForWidth())
        self.bday_comboBox.setSizePolicy(sizePolicy)
        self.bday_comboBox.setMinimumSize(QtCore.QSize(144, 51))
        self.bday_comboBox.setMaximumSize(QtCore.QSize(100, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bday_comboBox.setFont(font)
        self.bday_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.bday_comboBox.setObjectName("bday_comboBox")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.bday_comboBox.addItem("")
        self.byear_LE = QtWidgets.QLineEdit(self.frame)
        self.byear_LE.setGeometry(QtCore.QRect(790, 440, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.byear_LE.setFont(font)
        self.byear_LE.setObjectName("byear_LE")
        self.make_admin_checkbox = QtWidgets.QCheckBox(self.frame)
        self.make_admin_checkbox.setGeometry(QtCore.QRect(480, 530, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.make_admin_checkbox.setFont(font)
        self.make_admin_checkbox.setObjectName("make_admin_checkbox")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(480, 110, 111, 101))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("D:/Dev/Python/PyQT/AM/res/human-resources.svg"))
        self.Logo.setObjectName("Logo")
        self.back_button = QtWidgets.QPushButton(self.frame)
        self.back_button.setGeometry(QtCore.QRect(550, 630, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("")
        self.back_button.setObjectName("back_button")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(240, 574, 531, 51))
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

    def green_error_init(self):
        self.error_out.setStyleSheet("color: rgb(25, 235, 13);")

    def red_error_init(self):
        self.error_out.setStyleSheet("color: crimson;")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.close_button.setText(_translate("MainWindow", "x"))
        self.minimize_button.setText(_translate("MainWindow", "-"))
        self.drop_button.setText(_translate("MainWindow", "o"))
        self.AM_main_label.setText(_translate("MainWindow", "ATTENDANCE MANAGER"))
        self.login_label.setText(_translate("MainWindow", "CREATE NEW ACCOUNT"))
        self.FirstName_LE.setPlaceholderText(_translate("MainWindow", "FIRST NAME"))
        self.Password_LE.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.signup_button.setText(_translate("MainWindow", "SIGN UP"))
        self.LastName_LE.setPlaceholderText(_translate("MainWindow", "LAST NAME"))
        self.Email_LE.setPlaceholderText(_translate("MainWindow", "EMAIL"))
        self.cpassword_LE.setPlaceholderText(_translate("MainWindow", "CONFIRM PASSWORD"))
        self.Phone_LE.setPlaceholderText(_translate("MainWindow", "PHONE NUMBER"))
        self.bmonth_comboBox.setItemText(0, _translate("MainWindow", "January"))
        self.bmonth_comboBox.setItemText(1, _translate("MainWindow", "February"))
        self.bmonth_comboBox.setItemText(2, _translate("MainWindow", "March"))
        self.bmonth_comboBox.setItemText(3, _translate("MainWindow", "April"))
        self.bmonth_comboBox.setItemText(4, _translate("MainWindow", "May"))
        self.bmonth_comboBox.setItemText(5, _translate("MainWindow", "June"))
        self.bmonth_comboBox.setItemText(6, _translate("MainWindow", "July"))
        self.bmonth_comboBox.setItemText(7, _translate("MainWindow", "August"))
        self.bmonth_comboBox.setItemText(8, _translate("MainWindow", "September"))
        self.bmonth_comboBox.setItemText(9, _translate("MainWindow", "October"))
        self.bmonth_comboBox.setItemText(10, _translate("MainWindow", "November"))
        self.bmonth_comboBox.setItemText(11, _translate("MainWindow", "December"))
        self.bday_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.bday_comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.bday_comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.bday_comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.bday_comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.bday_comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.bday_comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.bday_comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.bday_comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.bday_comboBox.setItemText(9, _translate("MainWindow", "10"))
        self.bday_comboBox.setItemText(10, _translate("MainWindow", "11"))
        self.bday_comboBox.setItemText(11, _translate("MainWindow", "12"))
        self.bday_comboBox.setItemText(12, _translate("MainWindow", "13"))
        self.bday_comboBox.setItemText(13, _translate("MainWindow", "14"))
        self.bday_comboBox.setItemText(14, _translate("MainWindow", "15"))
        self.bday_comboBox.setItemText(15, _translate("MainWindow", "16"))
        self.bday_comboBox.setItemText(16, _translate("MainWindow", "17"))
        self.bday_comboBox.setItemText(17, _translate("MainWindow", "18"))
        self.bday_comboBox.setItemText(18, _translate("MainWindow", "19"))
        self.bday_comboBox.setItemText(19, _translate("MainWindow", "20"))
        self.bday_comboBox.setItemText(20, _translate("MainWindow", "21"))
        self.bday_comboBox.setItemText(21, _translate("MainWindow", "22"))
        self.bday_comboBox.setItemText(22, _translate("MainWindow", "23"))
        self.bday_comboBox.setItemText(23, _translate("MainWindow", "24"))
        self.bday_comboBox.setItemText(24, _translate("MainWindow", "25"))
        self.bday_comboBox.setItemText(25, _translate("MainWindow", "26"))
        self.bday_comboBox.setItemText(26, _translate("MainWindow", "27"))
        self.bday_comboBox.setItemText(27, _translate("MainWindow", "28"))
        self.bday_comboBox.setItemText(28, _translate("MainWindow", "29"))
        self.bday_comboBox.setItemText(29, _translate("MainWindow", "30"))
        self.bday_comboBox.setItemText(30, _translate("MainWindow", "31"))
        self.byear_LE.setPlaceholderText(_translate("MainWindow", "YEAR"))
        self.make_admin_checkbox.setText(_translate("MainWindow", "Make Admin"))
        self.back_button.setText(_translate("MainWindow", "BACK"))

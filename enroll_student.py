# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enroll_student.ui'
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
"QPushButton#enroll_button,QPushButton#back_button, QPushButton#capture_button{\n"
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
"QPushButton#enroll_button:hover,QPushButton#back_button:hover,QPushButton#capture_button:hover{\n"
"font-size: 16px;\n"
"border-top: 5px solid rgb(28, 235, 13);\n"
"border-bottom: 5px solid rgb(28, 235, 13);\n"
"border-left: 5px solid rgb(28, 235, 13);\n"
"border-right: 5px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton#enroll_button:pressed,QPushButton#back_button:pressed, QPushButton#capture_button:pressed{\n"
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
        self.AM_main_label.setGeometry(QtCore.QRect(130, 55, 431, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AM_main_label.setFont(font)
        self.AM_main_label.setStyleSheet("color: white;")
        self.AM_main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.AM_main_label.setObjectName("AM_main_label")
        self.ES_label = QtWidgets.QLabel(self.frame)
        self.ES_label.setGeometry(QtCore.QRect(10, 180, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ES_label.setFont(font)
        self.ES_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ES_label.setObjectName("ES_label")
        self.ES_FirstName_LE = QtWidgets.QLineEdit(self.frame)
        self.ES_FirstName_LE.setGeometry(QtCore.QRect(60, 240, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_FirstName_LE.setFont(font)
        self.ES_FirstName_LE.setObjectName("ES_FirstName_LE")
        self.ES_roll_LE = QtWidgets.QLineEdit(self.frame)
        self.ES_roll_LE.setGeometry(QtCore.QRect(60, 380, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_roll_LE.setFont(font)
        self.ES_roll_LE.setObjectName("ES_roll_LE")
        self.enroll_button = QtWidgets.QPushButton(self.frame)
        self.enroll_button.setGeometry(QtCore.QRect(240, 630, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.enroll_button.setFont(font)
        self.enroll_button.setStyleSheet("")
        self.enroll_button.setObjectName("enroll_button")
        self.ES_LastName_LE = QtWidgets.QLineEdit(self.frame)
        self.ES_LastName_LE.setGeometry(QtCore.QRect(360, 240, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_LastName_LE.setFont(font)
        self.ES_LastName_LE.setObjectName("ES_LastName_LE")
        self.ES_Email_LE = QtWidgets.QLineEdit(self.frame)
        self.ES_Email_LE.setGeometry(QtCore.QRect(60, 450, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_Email_LE.setFont(font)
        self.ES_Email_LE.setObjectName("ES_Email_LE")
        self.ES_Phone_LE = QtWidgets.QLineEdit(self.frame)
        self.ES_Phone_LE.setGeometry(QtCore.QRect(60, 520, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_Phone_LE.setFont(font)
        self.ES_Phone_LE.setToolTipDuration(3)
        self.ES_Phone_LE.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.ES_Phone_LE.setObjectName("ES_Phone_LE")
        self.ES_bmonth = QtWidgets.QComboBox(self.frame)
        self.ES_bmonth.setGeometry(QtCore.QRect(230, 310, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_bmonth.setFont(font)
        self.ES_bmonth.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.ES_bmonth.setObjectName("ES_bmonth")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bmonth.addItem("")
        self.ES_bday = QtWidgets.QComboBox(self.frame)
        self.ES_bday.setGeometry(QtCore.QRect(70, 310, 144, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ES_bday.sizePolicy().hasHeightForWidth())
        self.ES_bday.setSizePolicy(sizePolicy)
        self.ES_bday.setMinimumSize(QtCore.QSize(144, 51))
        self.ES_bday.setMaximumSize(QtCore.QSize(100, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_bday.setFont(font)
        self.ES_bday.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.ES_bday.setObjectName("ES_bday")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_bday.addItem("")
        self.ES_byear_LE = QtWidgets.QLineEdit(self.frame)
        self.ES_byear_LE.setGeometry(QtCore.QRect(410, 310, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_byear_LE.setFont(font)
        self.ES_byear_LE.setObjectName("ES_byear_LE")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 50, 111, 101))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("../res/human-resources.svg"))
        self.Logo.setObjectName("Logo")
        self.back_button = QtWidgets.QPushButton(self.frame)
        self.back_button.setGeometry(QtCore.QRect(890, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("")
        self.back_button.setObjectName("back_button")
        self.hline_sep = QtWidgets.QFrame(self.frame)
        self.hline_sep.setGeometry(QtCore.QRect(0, 150, 1061, 5))
        self.hline_sep.setStyleSheet("background: #222;")
        self.hline_sep.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline_sep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline_sep.setObjectName("hline_sep")
        self.ES_year_comboBox = QtWidgets.QComboBox(self.frame)
        self.ES_year_comboBox.setGeometry(QtCore.QRect(290, 380, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_year_comboBox.setFont(font)
        self.ES_year_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.ES_year_comboBox.setObjectName("ES_year_comboBox")
        self.ES_year_comboBox.addItem("")
        self.ES_year_comboBox.addItem("")
        self.ES_year_comboBox.addItem("")
        self.ES_year_comboBox.addItem("")
        self.ES_blood_comboBox = QtWidgets.QComboBox(self.frame)
        self.ES_blood_comboBox.setGeometry(QtCore.QRect(380, 450, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_blood_comboBox.setFont(font)
        self.ES_blood_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.ES_blood_comboBox.setObjectName("ES_blood_comboBox")
        self.ES_blood_comboBox.addItem("")
        self.ES_blood_comboBox.addItem("")
        self.ES_blood_comboBox.addItem("")
        self.ES_blood_comboBox.addItem("")
        self.ES_blood_comboBox.addItem("")
        self.ES_blood_comboBox.addItem("")
        self.ES_blood_comboBox.addItem("")
        self.ES_blood_comboBox.addItem("")
        self.capture_button = QtWidgets.QPushButton(self.frame)
        self.capture_button.setGeometry(QtCore.QRect(710, 600, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.capture_button.setFont(font)
        self.capture_button.setStyleSheet("")
        self.capture_button.setObjectName("capture_button")
        self.Uname_display = QtWidgets.QLabel(self.frame)
        self.Uname_display.setGeometry(QtCore.QRect(850, 50, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Uname_display.setFont(font)
        self.Uname_display.setStyleSheet("")
        self.Uname_display.setAlignment(QtCore.Qt.AlignCenter)
        self.Uname_display.setObjectName("Uname_display")
        self.dp = QtWidgets.QLabel(self.frame)
        self.dp.setGeometry(QtCore.QRect(775, 55, 71, 71))
        self.dp.setStyleSheet("border: 3px solid rgb(25,235,13);\n"
"border-radius: 35px;\n"
"")
        self.dp.setAlignment(QtCore.Qt.AlignCenter)
        self.dp.setObjectName("dp")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(20, 590, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.error_out.setFont(font)
        self.error_out.setStyleSheet("color: red;\n"
"padding-left: 20px;")
        self.error_out.setText("")
        self.error_out.setObjectName("error_out")
        self.display = QtWidgets.QLabel(self.frame)
        self.display.setGeometry(QtCore.QRect(630, 210, 391, 361))
        self.display.setStyleSheet("border: 3px solid rgb(25, 235, 13);\n"
"border-radius: 10px;")
        self.display.setAlignment(QtCore.Qt.AlignCenter)
        self.display.setObjectName("display")
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
        self.ES_label.setText(_translate("MainWindow", "ENROLL STUDENT"))
        self.ES_FirstName_LE.setPlaceholderText(_translate("MainWindow", "FIRST NAME"))
        self.ES_roll_LE.setPlaceholderText(_translate("MainWindow", "ROLL NUMBER"))
        self.enroll_button.setText(_translate("MainWindow", "ENROLL"))
        self.ES_LastName_LE.setPlaceholderText(_translate("MainWindow", "LAST NAME"))
        self.ES_Email_LE.setPlaceholderText(_translate("MainWindow", "EMAIL"))
        self.ES_Phone_LE.setPlaceholderText(_translate("MainWindow", "PHONE NUMBER"))
        self.ES_bmonth.setItemText(0, _translate("MainWindow", "January"))
        self.ES_bmonth.setItemText(1, _translate("MainWindow", "February"))
        self.ES_bmonth.setItemText(2, _translate("MainWindow", "March"))
        self.ES_bmonth.setItemText(3, _translate("MainWindow", "April"))
        self.ES_bmonth.setItemText(4, _translate("MainWindow", "May"))
        self.ES_bmonth.setItemText(5, _translate("MainWindow", "June"))
        self.ES_bmonth.setItemText(6, _translate("MainWindow", "July"))
        self.ES_bmonth.setItemText(7, _translate("MainWindow", "August"))
        self.ES_bmonth.setItemText(8, _translate("MainWindow", "September"))
        self.ES_bmonth.setItemText(9, _translate("MainWindow", "October"))
        self.ES_bmonth.setItemText(10, _translate("MainWindow", "November"))
        self.ES_bmonth.setItemText(11, _translate("MainWindow", "December"))
        self.ES_bday.setItemText(0, _translate("MainWindow", "1"))
        self.ES_bday.setItemText(1, _translate("MainWindow", "2"))
        self.ES_bday.setItemText(2, _translate("MainWindow", "3"))
        self.ES_bday.setItemText(3, _translate("MainWindow", "4"))
        self.ES_bday.setItemText(4, _translate("MainWindow", "5"))
        self.ES_bday.setItemText(5, _translate("MainWindow", "6"))
        self.ES_bday.setItemText(6, _translate("MainWindow", "7"))
        self.ES_bday.setItemText(7, _translate("MainWindow", "8"))
        self.ES_bday.setItemText(8, _translate("MainWindow", "9"))
        self.ES_bday.setItemText(9, _translate("MainWindow", "10"))
        self.ES_bday.setItemText(10, _translate("MainWindow", "11"))
        self.ES_bday.setItemText(11, _translate("MainWindow", "12"))
        self.ES_bday.setItemText(12, _translate("MainWindow", "13"))
        self.ES_bday.setItemText(13, _translate("MainWindow", "14"))
        self.ES_bday.setItemText(14, _translate("MainWindow", "15"))
        self.ES_bday.setItemText(15, _translate("MainWindow", "16"))
        self.ES_bday.setItemText(16, _translate("MainWindow", "17"))
        self.ES_bday.setItemText(17, _translate("MainWindow", "18"))
        self.ES_bday.setItemText(18, _translate("MainWindow", "19"))
        self.ES_bday.setItemText(19, _translate("MainWindow", "20"))
        self.ES_bday.setItemText(20, _translate("MainWindow", "21"))
        self.ES_bday.setItemText(21, _translate("MainWindow", "22"))
        self.ES_bday.setItemText(22, _translate("MainWindow", "23"))
        self.ES_bday.setItemText(23, _translate("MainWindow", "24"))
        self.ES_bday.setItemText(24, _translate("MainWindow", "25"))
        self.ES_bday.setItemText(25, _translate("MainWindow", "26"))
        self.ES_bday.setItemText(26, _translate("MainWindow", "27"))
        self.ES_bday.setItemText(27, _translate("MainWindow", "28"))
        self.ES_bday.setItemText(28, _translate("MainWindow", "29"))
        self.ES_bday.setItemText(29, _translate("MainWindow", "30"))
        self.ES_bday.setItemText(30, _translate("MainWindow", "31"))
        self.ES_byear_LE.setPlaceholderText(_translate("MainWindow", "YEAR"))
        self.back_button.setText(_translate("MainWindow", "SIGN OUT"))
        self.ES_year_comboBox.setItemText(0, _translate("MainWindow", "1st Year"))
        self.ES_year_comboBox.setItemText(1, _translate("MainWindow", "2nd Year"))
        self.ES_year_comboBox.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.ES_year_comboBox.setItemText(3, _translate("MainWindow", "4th Year"))
        self.ES_blood_comboBox.setItemText(0, _translate("MainWindow", "A+"))
        self.ES_blood_comboBox.setItemText(1, _translate("MainWindow", "B+"))
        self.ES_blood_comboBox.setItemText(2, _translate("MainWindow", "AB+"))
        self.ES_blood_comboBox.setItemText(3, _translate("MainWindow", "O+"))
        self.ES_blood_comboBox.setItemText(4, _translate("MainWindow", "A-"))
        self.ES_blood_comboBox.setItemText(5, _translate("MainWindow", "B-"))
        self.ES_blood_comboBox.setItemText(6, _translate("MainWindow", "AB-"))
        self.ES_blood_comboBox.setItemText(7, _translate("MainWindow", "O-"))
        self.capture_button.setText(_translate("MainWindow", "CAPTURE"))
        self.Uname_display.setText(_translate("MainWindow", "USERNAME"))
        self.dp.setText(_translate("MainWindow", "No Preview"))
        self.display.setText(_translate("MainWindow", "No Preview"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conifg_pop.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(875, 642)
        Dialog.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 831, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame{\n"
"border-radius: 16px;\n"
"background: black;\n"
"}\n"
"\n"
"QFrame#top_bar{\n"
"border-radius: 10px;\n"
"background: #222;\n"
"}\n"
"\n"
"QLine{\n"
"background: #222;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
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
"QPushButton{\n"
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
"QPushButton:hover{\n"
"font-size: 16px;\n"
"border-top: 5px solid rgba(28, 235, 13, 1);\n"
"border-bottom: 5px solid rgba(28, 235, 13, 1);\n"
"border-left: 5px solid rgba(28, 235, 13, 1);\n"
"border-right: 5px solid rgba(28, 235, 13, 1);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-size: 12px;\n"
"background-color: rgb(32, 177, 16);\n"
"border-top: 5px solid transparent;\n"
"border-bottom: 5px solid transparent;\n"
"border-left: 5px solid transparent;\n"
"border-right: 5px solid transparent;\n"
"}\n"
"\n"
"QLabel{\n"
" color: rgb(25,235,13);\n"
"padding-left: 15px;\n"
"background: black;\n"
"}\n"
"\n"
"QLabel#error_out {\n"
"background: transparent;\n"
"color: crimson;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#close_button{\n"
"color: transparent;\n"
"border-radius: 10px;\n"
"background: red;\n"
"}\n"
"\n"
"QPushButton#close_button:hover {\n"
"background: red;\n"
"color: black;\n"
"border: 4px red solid;\n"
"}\n"
"\n"
"QPushButton#drop_button{\n"
"background: red;\n"
"color: transparent;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#drop_button:hover {\n"
"background: red;\n"
"color: black;\n"
"border: 4px red solid;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.top_bar = QtWidgets.QFrame(self.frame)
        self.top_bar.setGeometry(QtCore.QRect(0, 0, 831, 35))
        self.top_bar.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_bar.setObjectName("top_bar")
        self.drop = QtWidgets.QPushButton(self.frame)
        self.drop.setGeometry(QtCore.QRect(360, 510, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.drop.setFont(font)
        self.drop.setObjectName("drop")
        self.close_button = QtWidgets.QPushButton(self.frame)
        self.close_button.setGeometry(QtCore.QRect(800, 10, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("background-color: crimson;\n"
"padding-bottom: 4px;")
        self.close_button.setObjectName("close_button")
        self.drop_button = QtWidgets.QPushButton(self.frame)
        self.drop_button.setGeometry(QtCore.QRect(770, 10, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.drop_button.setFont(font)
        self.drop_button.setStyleSheet("border-radius: 10px; \n"
"background-color: rgb(84, 206, 28);\n"
"padding-bottom: 4px;\n"
"padding-left: 2px;\n"
"")
        self.drop_button.setObjectName("drop_button")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(0, 466, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.error_out.setFont(font)
        self.error_out.setStyleSheet("color: crimson;")
        self.error_out.setText("")
        self.error_out.setAlignment(QtCore.Qt.AlignCenter)
        self.error_out.setObjectName("error_out")
        self.db_username = QtWidgets.QLineEdit(self.frame)
        self.db_username.setGeometry(QtCore.QRect(226, 60, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.db_username.setFont(font)
        self.db_username.setText("")
        self.db_username.setObjectName("db_username")
        self.db_password = QtWidgets.QLineEdit(self.frame)
        self.db_password.setGeometry(QtCore.QRect(226, 130, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.db_password.setFont(font)
        self.db_password.setText("")
        self.db_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.db_password.setObjectName("db_password")
        self.db_ip = QtWidgets.QLineEdit(self.frame)
        self.db_ip.setGeometry(QtCore.QRect(226, 200, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.db_ip.setFont(font)
        self.db_ip.setText("")
        self.db_ip.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.db_ip.setObjectName("db_ip")
        self.db_port = QtWidgets.QLineEdit(self.frame)
        self.db_port.setGeometry(QtCore.QRect(460, 200, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.db_port.setFont(font)
        self.db_port.setText("")
        self.db_port.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.db_port.setObjectName("db_port")
        self.stb_name = QtWidgets.QLineEdit(self.frame)
        self.stb_name.setGeometry(QtCore.QRect(226, 340, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stb_name.setFont(font)
        self.stb_name.setText("")
        self.stb_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.stb_name.setObjectName("stb_name")
        self.utb_name = QtWidgets.QLineEdit(self.frame)
        self.utb_name.setGeometry(QtCore.QRect(226, 270, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.utb_name.setFont(font)
        self.utb_name.setText("")
        self.utb_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.utb_name.setObjectName("utb_name")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(377, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"background: transparent;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.admin_password = QtWidgets.QLineEdit(self.frame)
        self.admin_password.setGeometry(QtCore.QRect(440, 409, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.admin_password.setFont(font)
        self.admin_password.setText("")
        self.admin_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.admin_password.setObjectName("admin_password")
        self.admin_uname = QtWidgets.QLineEdit(self.frame)
        self.admin_uname.setGeometry(QtCore.QRect(150, 410, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.admin_uname.setFont(font)
        self.admin_uname.setText("")
        self.admin_uname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.admin_uname.setObjectName("admin_uname")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.top_bar.mouseMoveEvent = self.movewindow

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.drop.setText(_translate("Dialog", "SAVE"))
        self.close_button.setText(_translate("Dialog", "x"))
        self.drop_button.setText(_translate("Dialog", "-"))
        self.db_username.setPlaceholderText(_translate("Dialog", "DATABASE USERNAME"))
        self.db_password.setPlaceholderText(_translate("Dialog", "DATABASE PASSWORD"))
        self.db_ip.setPlaceholderText(_translate("Dialog", "DB IP"))
        self.db_port.setPlaceholderText(_translate("Dialog", "DB PORT"))
        self.stb_name.setPlaceholderText(_translate("Dialog", " STUDENT MAIN TABLE NAME"))
        self.utb_name.setPlaceholderText(_translate("Dialog", "USER IO TABLE"))
        self.label.setText(_translate("Dialog", "Settings"))
        self.admin_password.setPlaceholderText(_translate("Dialog", "PASSWORD"))
        self.admin_uname.setPlaceholderText(_translate("Dialog", "ADMIN USER NAME"))

    def mousePressEvent(self, event):       
        self.dragPos = event.globalPos()

    def movewindow(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
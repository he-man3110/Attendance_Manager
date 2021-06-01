# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drop_sub_pop.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 407)
        Dialog.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 641, 391))
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
"Line{\n"
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
"border-top: 5px solid rgb(28, 235, 13);\n"
"border-bottom: 5px solid rgb(28, 235, 13);\n"
"border-left: 5px solid rgb(28, 235, 13);\n"
"border-right: 5px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-size: 12px;\n"
"background-color: rgb(32, 177, 16);\n"
"border-top: 5px solid black;\n"
"border-bottom: 5px solid black;\n"
"border-left: 5px solid black;\n"
"border-right: 5px solid black;\n"
"}\n"
"\n"
"QListView{\n"
"background: black;\n"
"color: white;\n"
"}\n"
"\n"
"QListView:hover{\n"
"background: blue;\n"
"color: white;\n"
"}\n"
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
"}\n"
"\n"
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
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.top_bar = QtWidgets.QFrame(self.frame)
        self.top_bar.setGeometry(QtCore.QRect(0, 0, 641, 35))
        self.top_bar.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_bar.setObjectName("top_bar")
        self.drop = QtWidgets.QPushButton(self.frame)
        self.drop.setGeometry(QtCore.QRect(250, 320, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.drop.setFont(font)
        self.drop.setObjectName("drop")
        self.close_button = QtWidgets.QPushButton(self.frame)
        self.close_button.setGeometry(QtCore.QRect(600, 10, 21, 21))
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
        self.drop_button.setGeometry(QtCore.QRect(570, 10, 21, 21))
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
        self.subject_list = QtWidgets.QComboBox(self.frame)
        self.subject_list.setGeometry(QtCore.QRect(110, 70, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject_list.setFont(font)
        self.subject_list.setCurrentText("")
        self.subject_list.setObjectName("subject_list")
        self.save_details = QtWidgets.QCheckBox(self.frame)
        self.save_details.setGeometry(QtCore.QRect(190, 140, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_details.setFont(font)
        self.save_details.setObjectName("save_details")
        self.location = QtWidgets.QLineEdit(self.frame)
        self.location.setGeometry(QtCore.QRect(20, 200, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.location.setFont(font)
        self.location.setObjectName("location")
        self.browse = QtWidgets.QPushButton(self.frame)
        self.browse.setGeometry(QtCore.QRect(490, 200, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.browse.setFont(font)
        self.browse.setObjectName("browse")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(10, 270, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.error_out.setFont(font)
        self.error_out.setStyleSheet("color: crimson;")
        self.error_out.setText("")
        self.error_out.setAlignment(QtCore.Qt.AlignCenter)
        self.error_out.setObjectName("error_out")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #custom
        self.top_bar.mouseMoveEvent = self.movewindow

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.drop.setText(_translate("Dialog", "DROP"))
        self.close_button.setText(_translate("Dialog", "x"))
        self.drop_button.setText(_translate("Dialog", "-"))
        self.save_details.setText(_translate("Dialog", "Save attendance detials"))
        self.location.setText(_translate("Dialog", "Location"))
        self.browse.setText(_translate("Dialog", "BROWSE"))

    def mousePressEvent(self, event):       
        self.dragPos = event.globalPos()

    def movewindow(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

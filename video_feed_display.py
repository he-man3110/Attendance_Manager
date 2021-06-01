# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_feed_display.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 717)
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
        self.frame.setGeometry(QtCore.QRect(10, 0, 1061, 701))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame#view_attendance_frame, QFrame#enroll_student_frame, QFrame#view_subject_frame, QFrame#mark_attendance_frame{\n"
"background: black;\n"
"border-radius: 14px;\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"\n"
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
"QPushButton#mark_manual, QPushButton#stop_button, QPushButton#VA_button, QPushButton#ES_enroll_button,\n"
"QPushButton#sign_out_button, QPushButton#MA_mark_button, QPushButton#manage_accounts_button, QPushButton#add_subjects_button {\n"
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
"QPushButton#mark_manual:hover, QPushButton#stop_button:hover, QPushButton#VA_button:hover, QPushButton#ES_enroll_button:hover, QPushButton#sign_out_button:hover, QPushButton#MA_mark_button:hover,\n"
"QPushButton#manage_accounts_button:hover,QPushButton#add_subjects_button:hover {\n"
"font-size: 16px;\n"
"border-top: 5px solid rgb(28, 235, 13);\n"
"border-bottom: 5px solid rgb(28, 235, 13);\n"
"border-left: 5px solid rgb(28, 235, 13);\n"
"border-right: 5px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton#mark_manual:pressed, QPushButton#stop_button:pressed, QPushButton#VA_button:pressed,QPushButton#ES_enroll_button:pressed,\n"
"QPushButton#sign_out_button:pressed,QPushButton#MA_mark_button:pressed,\n"
"QPushButton#manage_accounts_button:pressed,QPushButton#add_subjects_button:pressed {\n"
"font-size: 12px;\n"
"background-color: rgb(32, 177, 16);\n"
"border-top: 5px solid black;\n"
"border-bottom: 5px solid black;\n"
"border-left: 5px solid black;\n"
"border-right: 5px solid black;\n"
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
"QLabel#image_preview_window{\n"
"border: 3px ridge rgb(25, 235, 13);\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"background: #222;\n"
"border-radius: 8px;\n"
"border: 2px solid #222;\n"
"}\n"
"\n"
"QScrollBar::sub-line{\n"
"color: #222;\n"
"background: #222;\n"
"width: 10px;\n"
"}\n"
"\n"
"QScrollBar::sub-page{\n"
"background: #222;\n"
"}\n"
"\n"
"QScrollBar::add-page{\n"
"background: #222;\n"
"}\n"
"\n"
"QScrollBar::add-line{\n"
"background: #222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background: rgb(144,144,144);\n"
"border: 3px solid #222;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background: rgb(96,96,96);\n"
"border-radius: 8px;\n"
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
        self.AM_main_label.setGeometry(QtCore.QRect(140, 50, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AM_main_label.setFont(font)
        self.AM_main_label.setStyleSheet("color: white;")
        self.AM_main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.AM_main_label.setObjectName("AM_main_label")
        self.disp_username_label = QtWidgets.QLabel(self.frame)
        self.disp_username_label.setGeometry(QtCore.QRect(860, 50, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.disp_username_label.setFont(font)
        self.disp_username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.disp_username_label.setObjectName("disp_username_label")
        self.image_preview_window = QtWidgets.QLabel(self.frame)
        self.image_preview_window.setGeometry(QtCore.QRect(775, 55, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.image_preview_window.setFont(font)
        self.image_preview_window.setStyleSheet("border: 3px solid rgb(25,235,13);\n"
"border-radius: 35px;")
        self.image_preview_window.setAlignment(QtCore.Qt.AlignCenter)
        self.image_preview_window.setObjectName("image_preview_window")
        self.hline_sep = QtWidgets.QFrame(self.frame)
        self.hline_sep.setGeometry(QtCore.QRect(0, 140, 1061, 5))
        self.hline_sep.setStyleSheet("background: #222;")
        self.hline_sep.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline_sep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline_sep.setObjectName("hline_sep")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 45, 101, 91))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("D:/Dev/Python/PyQT/AM/res/human-resources.svg"))
        self.Logo.setObjectName("Logo")
        self.stop_button = QtWidgets.QPushButton(self.frame)
        self.stop_button.setGeometry(QtCore.QRect(895, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet("")
        self.stop_button.setObjectName("stop_button")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(250, 644, 811, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.error_out.setFont(font)
        self.error_out.setStyleSheet("color: crimson;")
        self.error_out.setText("")
        self.error_out.setAlignment(QtCore.Qt.AlignCenter)
        self.error_out.setObjectName("error_out")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(20, 180, 231, 511))
        self.scrollArea.setStyleSheet("background: #222;\n"
"border-radius: 8px;\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 214, 511))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.recognize_label = QtWidgets.QLabel(self.frame)
        self.recognize_label.setGeometry(QtCore.QRect(2, 152, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.recognize_label.setFont(font)
        self.recognize_label.setStyleSheet("")
        self.recognize_label.setAlignment(QtCore.Qt.AlignCenter)
        self.recognize_label.setObjectName("recognize_label")
        self.mark_manual = QtWidgets.QPushButton(self.frame)
        self.mark_manual.setGeometry(QtCore.QRect(570, 70, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mark_manual.setFont(font)
        self.mark_manual.setObjectName("mark_manual")
        self.video_out = QtWidgets.QLabel(self.frame)
        self.video_out.setGeometry(QtCore.QRect(270, 160, 771, 471))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.video_out.setFont(font)
        self.video_out.setStyleSheet("border: 3px solid white;\n"
"border-radius: 8px;")
        self.video_out.setAlignment(QtCore.Qt.AlignCenter)
        self.video_out.setObjectName("video_out")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #custom
        self.gbox = QtWidgets.QGroupBox()
        self.formwin = QtWidgets.QFormLayout()
        self.gbox.setLayout(self.formwin)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidget(self.gbox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedHeight(511)
        #self.add_labels()

    def cButtoname(self, string):
        _translate = QtCore.QCoreApplication.translate
        self.stop_button.setText(_translate("MainWindow", string))     

    def add_label(self, name):
        temp = QtWidgets.QLabel(name)
        temp.setMaximumSize(192, 30)
        temp.setMinimumSize(192, 30)
        temp.setStyleSheet("background: black;\nborder-radius: 8px;\npadding-left: 20px;\ncolor: rgb(25, 235, 13);\n")
        self.formwin.addRow(temp)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.close_button.setText(_translate("MainWindow", "x"))
        self.minimize_button.setText(_translate("MainWindow", "-"))
        self.drop_button.setText(_translate("MainWindow", "o"))
        self.AM_main_label.setText(_translate("MainWindow", "ATTENDANCE MANAGER"))
        self.disp_username_label.setText(_translate("MainWindow", "USERNAME"))
        self.image_preview_window.setText(_translate("MainWindow", "No Preview"))
        self.stop_button.setText(_translate("MainWindow", "STOP"))
        self.recognize_label.setText(_translate("MainWindow", "RECOGNIZED"))
        self.mark_manual.setText(_translate("MainWindow", "MARK"))
        self.video_out.setText(_translate("MainWindow", "TextLabel"))

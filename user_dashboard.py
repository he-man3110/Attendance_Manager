# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_dashboard.ui'
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
        self.frame.setGeometry(QtCore.QRect(9, 9, 1061, 701))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame#view_attendance_frame, QFrame#add_subject_frame, QFrame#view_subject_stats_frame, QFrame#mark_attendance_frame{\n"
"background: black;\n"
"border-radius: 14px;\n"
"border: 3px solid white;\n"
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
"QPushButton#MA_button, QPushButton#capture_button, QPushButton#VSS_button, QPushButton#AS_button,\n"
"QPushButton#VA_button,QPushButton#signout_button{\n"
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
"QPushButton#MA_button:hover, QPushButton#capture_button:hover, QPushButton#VSS:hover, QPushButton#AS_button:hover,QPushButton#VA_button:hover,QPushButton#signout_button:hover{\n"
"font-size: 16px;\n"
"border-top: 5px solid rgb(28, 235, 13);\n"
"border-bottom: 5px solid rgb(28, 235, 13);\n"
"border-left: 5px solid rgb(28, 235, 13);\n"
"border-right: 5px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton#MA_button:pressed, QPushButton#capture_button:pressed, QPushButton#VSS_button:pressed,QPushButton#AS_button:pressed, QPushButton#VA_button:pressed,\n"
"QPushButton#signout_button:pressed{\n"
"font-size: 12px;\n"
"background-color: rgb(32, 177, 16);\n"
"border-top: 5px solid black;\n"
"border-bottom: 5px solid black;\n"
"border-left: 5px solid black;\n"
"border-right: 5px solid black;\n"
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
"QListView{\n"
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
"QComboBox:editable {\n"
"background: black;\n"
"color: blue;\n"
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
"    background: black;\n"
"    color: white;\n"
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
"    color: white;\n"
"    background: blue;\n"
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
"QLabel#image_preview_window{\n"
"border: 3px ridge rgb(25, 235, 13);\n"
"border-radius: 12px;\n"
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
        self.dp_preview_window = QtWidgets.QLabel(self.frame)
        self.dp_preview_window.setGeometry(QtCore.QRect(775, 55, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dp_preview_window.setFont(font)
        self.dp_preview_window.setStyleSheet("border-radius: 35px;\n"
"border: 3px solid rgb(25, 235, 13);")
        self.dp_preview_window.setAlignment(QtCore.Qt.AlignCenter)
        self.dp_preview_window.setObjectName("dp_preview_window")
        self.vline_sep = QtWidgets.QFrame(self.frame)
        self.vline_sep.setGeometry(QtCore.QRect(251, 140, 5, 561))
        self.vline_sep.setStyleSheet("background: #222;")
        self.vline_sep.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline_sep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline_sep.setObjectName("vline_sep")
        self.hline_sep = QtWidgets.QFrame(self.frame)
        self.hline_sep.setGeometry(QtCore.QRect(0, 140, 1061, 5))
        self.hline_sep.setStyleSheet("background: #222;")
        self.hline_sep.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline_sep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline_sep.setObjectName("hline_sep")
        self.view_attendance_frame = QtWidgets.QFrame(self.frame)
        self.view_attendance_frame.setGeometry(QtCore.QRect(280, 160, 381, 241))
        self.view_attendance_frame.setStyleSheet("")
        self.view_attendance_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.view_attendance_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.view_attendance_frame.setObjectName("view_attendance_frame")
        self.view_attendance_label = QtWidgets.QLabel(self.view_attendance_frame)
        self.view_attendance_label.setGeometry(QtCore.QRect(10, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.view_attendance_label.setFont(font)
        self.view_attendance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_attendance_label.setObjectName("view_attendance_label")
        self.VA_year = QtWidgets.QComboBox(self.view_attendance_frame)
        self.VA_year.setGeometry(QtCore.QRect(20, 60, 160, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VA_year.sizePolicy().hasHeightForWidth())
        self.VA_year.setSizePolicy(sizePolicy)
        self.VA_year.setMinimumSize(QtCore.QSize(144, 51))
        self.VA_year.setMaximumSize(QtCore.QSize(160, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VA_year.setFont(font)
        self.VA_year.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VA_year.setObjectName("VA_year")
        self.VA_year.addItem("")
        self.VA_year.addItem("")
        self.VA_year.addItem("")
        self.VA_year.addItem("")
        self.VA_section = QtWidgets.QComboBox(self.view_attendance_frame)
        self.VA_section.setGeometry(QtCore.QRect(200, 60, 144, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VA_section.setFont(font)
        self.VA_section.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VA_section.setObjectName("VA_section")
        self.VA_section.addItem("")
        self.VA_section.addItem("")
        self.VA_roll_LE = QtWidgets.QLineEdit(self.view_attendance_frame)
        self.VA_roll_LE.setGeometry(QtCore.QRect(20, 120, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VA_roll_LE.setFont(font)
        self.VA_roll_LE.setObjectName("VA_roll_LE")
        self.VA_view_all = QtWidgets.QCheckBox(self.view_attendance_frame)
        self.VA_view_all.setGeometry(QtCore.QRect(240, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.VA_view_all.setFont(font)
        self.VA_view_all.setObjectName("VA_view_all")
        self.VA_button = QtWidgets.QPushButton(self.view_attendance_frame)
        self.VA_button.setGeometry(QtCore.QRect(90, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.VA_button.setFont(font)
        self.VA_button.setStyleSheet("")
        self.VA_button.setObjectName("VA_button")
        self.add_subject_frame = QtWidgets.QFrame(self.frame)
        self.add_subject_frame.setGeometry(QtCore.QRect(280, 420, 381, 241))
        self.add_subject_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_subject_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_subject_frame.setObjectName("add_subject_frame")
        self.add_subject_label = QtWidgets.QLabel(self.add_subject_frame)
        self.add_subject_label.setGeometry(QtCore.QRect(10, 10, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_subject_label.setFont(font)
        self.add_subject_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add_subject_label.setObjectName("add_subject_label")
        self.AS_year = QtWidgets.QComboBox(self.add_subject_frame)
        self.AS_year.setGeometry(QtCore.QRect(20, 120, 160, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AS_year.sizePolicy().hasHeightForWidth())
        self.AS_year.setSizePolicy(sizePolicy)
        self.AS_year.setMinimumSize(QtCore.QSize(144, 51))
        self.AS_year.setMaximumSize(QtCore.QSize(160, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AS_year.setFont(font)
        self.AS_year.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.AS_year.setObjectName("AS_year")
        self.AS_year.addItem("")
        self.AS_year.addItem("")
        self.AS_year.addItem("")
        self.AS_year.addItem("")
        self.AS_button = QtWidgets.QPushButton(self.add_subject_frame)
        self.AS_button.setGeometry(QtCore.QRect(90, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.AS_button.setFont(font)
        self.AS_button.setStyleSheet("")
        self.AS_button.setObjectName("AS_button")
        self.AS_section = QtWidgets.QComboBox(self.add_subject_frame)
        self.AS_section.setGeometry(QtCore.QRect(200, 120, 144, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AS_section.sizePolicy().hasHeightForWidth())
        self.AS_section.setSizePolicy(sizePolicy)
        self.AS_section.setMinimumSize(QtCore.QSize(144, 51))
        self.AS_section.setMaximumSize(QtCore.QSize(160, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AS_section.setFont(font)
        self.AS_section.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.AS_section.setObjectName("AS_section")
        self.AS_section.addItem("")
        self.AS_section.addItem("")
        self.AS_subject_list = QtWidgets.QComboBox(self.add_subject_frame)
        self.AS_subject_list.setGeometry(QtCore.QRect(20, 60, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AS_subject_list.sizePolicy().hasHeightForWidth())
        self.AS_subject_list.setSizePolicy(sizePolicy)
        self.AS_subject_list.setMinimumSize(QtCore.QSize(144, 51))
        self.AS_subject_list.setMaximumSize(QtCore.QSize(321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AS_subject_list.setFont(font)
        self.AS_subject_list.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.AS_subject_list.setCurrentText("")
        self.AS_subject_list.setObjectName("AS_subject_list")
        self.view_subject_stats_frame = QtWidgets.QFrame(self.frame)
        self.view_subject_stats_frame.setGeometry(QtCore.QRect(680, 160, 351, 241))
        self.view_subject_stats_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.view_subject_stats_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.view_subject_stats_frame.setObjectName("view_subject_stats_frame")
        self.view_subject_stats_label = QtWidgets.QLabel(self.view_subject_stats_frame)
        self.view_subject_stats_label.setGeometry(QtCore.QRect(10, 10, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.view_subject_stats_label.setFont(font)
        self.view_subject_stats_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_subject_stats_label.setObjectName("view_subject_stats_label")
        self.VSS_year = QtWidgets.QComboBox(self.view_subject_stats_frame)
        self.VSS_year.setGeometry(QtCore.QRect(20, 60, 160, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VSS_year.sizePolicy().hasHeightForWidth())
        self.VSS_year.setSizePolicy(sizePolicy)
        self.VSS_year.setMinimumSize(QtCore.QSize(144, 51))
        self.VSS_year.setMaximumSize(QtCore.QSize(160, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VSS_year.setFont(font)
        self.VSS_year.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VSS_year.setObjectName("VSS_year")
        self.VSS_year.addItem("")
        self.VSS_year.addItem("")
        self.VSS_year.addItem("")
        self.VSS_year.addItem("")
        self.VSS_section = QtWidgets.QComboBox(self.view_subject_stats_frame)
        self.VSS_section.setGeometry(QtCore.QRect(180, 60, 144, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VSS_section.setFont(font)
        self.VSS_section.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VSS_section.setObjectName("VSS_section")
        self.VSS_section.addItem("")
        self.VSS_section.addItem("")
        self.VSS_button = QtWidgets.QPushButton(self.view_subject_stats_frame)
        self.VSS_button.setGeometry(QtCore.QRect(80, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.VSS_button.setFont(font)
        self.VSS_button.setStyleSheet("")
        self.VSS_button.setObjectName("VSS_button")
        self.mark_attendance_frame = QtWidgets.QFrame(self.frame)
        self.mark_attendance_frame.setGeometry(QtCore.QRect(680, 420, 351, 241))
        self.mark_attendance_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mark_attendance_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mark_attendance_frame.setObjectName("mark_attendance_frame")
        self.mark_attendance_label = QtWidgets.QLabel(self.mark_attendance_frame)
        self.mark_attendance_label.setGeometry(QtCore.QRect(10, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mark_attendance_label.setFont(font)
        self.mark_attendance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mark_attendance_label.setObjectName("mark_attendance_label")
        self.MA_year = QtWidgets.QComboBox(self.mark_attendance_frame)
        self.MA_year.setGeometry(QtCore.QRect(20, 60, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MA_year.setFont(font)
        self.MA_year.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.MA_year.setObjectName("MA_year")
        self.MA_year.addItem("")
        self.MA_year.addItem("")
        self.MA_year.addItem("")
        self.MA_year.addItem("")
        self.MA_button = QtWidgets.QPushButton(self.mark_attendance_frame)
        self.MA_button.setGeometry(QtCore.QRect(20, 170, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.MA_button.setFont(font)
        self.MA_button.setStyleSheet("")
        self.MA_button.setObjectName("MA_button")
        self.MA_section = QtWidgets.QComboBox(self.mark_attendance_frame)
        self.MA_section.setGeometry(QtCore.QRect(175, 60, 144, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MA_section.setFont(font)
        self.MA_section.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.MA_section.setObjectName("MA_section")
        self.MA_section.addItem("")
        self.MA_section.addItem("")
        self.MA_subject_list = QtWidgets.QComboBox(self.mark_attendance_frame)
        self.MA_subject_list.setGeometry(QtCore.QRect(19, 114, 301, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MA_subject_list.sizePolicy().hasHeightForWidth())
        self.MA_subject_list.setSizePolicy(sizePolicy)
        self.MA_subject_list.setMinimumSize(QtCore.QSize(144, 51))
        self.MA_subject_list.setMaximumSize(QtCore.QSize(321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MA_subject_list.setFont(font)
        self.MA_subject_list.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.MA_subject_list.setCurrentText("")
        self.MA_subject_list.setObjectName("MA_subject_list")
        self.hline_prof_sep = QtWidgets.QFrame(self.frame)
        self.hline_prof_sep.setGeometry(QtCore.QRect(0, 190, 251, 5))
        self.hline_prof_sep.setStyleSheet("background: #222;")
        self.hline_prof_sep.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline_prof_sep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline_prof_sep.setObjectName("hline_prof_sep")
        self.SH_label = QtWidgets.QLabel(self.frame)
        self.SH_label.setGeometry(QtCore.QRect(0, 150, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SH_label.setFont(font)
        self.SH_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SH_label.setObjectName("SH_label")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 45, 101, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Dev/Python/PyQT/AM/res/human-resources.svg"))
        self.label.setObjectName("label")
        self.signout_button = QtWidgets.QPushButton(self.frame)
        self.signout_button.setGeometry(QtCore.QRect(895, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.signout_button.setFont(font)
        self.signout_button.setStyleSheet("")
        self.signout_button.setObjectName("signout_button")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(260, 660, 801, 41))
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
        self.SH_1 = QtWidgets.QLabel(self.frame)
        self.SH_1.setGeometry(QtCore.QRect(0, 210, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SH_1.setFont(font)
        self.SH_1.setText("")
        self.SH_1.setAlignment(QtCore.Qt.AlignCenter)
        self.SH_1.setObjectName("SH_1")
        self.SH_2 = QtWidgets.QLabel(self.frame)
        self.SH_2.setGeometry(QtCore.QRect(0, 270, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SH_2.setFont(font)
        self.SH_2.setText("")
        self.SH_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SH_2.setObjectName("SH_2")
        self.SH_4 = QtWidgets.QLabel(self.frame)
        self.SH_4.setGeometry(QtCore.QRect(0, 390, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SH_4.setFont(font)
        self.SH_4.setText("")
        self.SH_4.setAlignment(QtCore.Qt.AlignCenter)
        self.SH_4.setObjectName("SH_4")
        self.SH_3 = QtWidgets.QLabel(self.frame)
        self.SH_3.setGeometry(QtCore.QRect(0, 330, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SH_3.setFont(font)
        self.SH_3.setText("")
        self.SH_3.setAlignment(QtCore.Qt.AlignCenter)
        self.SH_3.setObjectName("SH_3")
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
        self.disp_username_label.setText(_translate("MainWindow", "USERNAME"))
        self.dp_preview_window.setText(_translate("MainWindow", "No Preview"))
        self.view_attendance_label.setText(_translate("MainWindow", "VIEW ATTENDANCE"))
        self.VA_year.setItemText(0, _translate("MainWindow", "1st Year"))
        self.VA_year.setItemText(1, _translate("MainWindow", "2nd year"))
        self.VA_year.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.VA_year.setItemText(3, _translate("MainWindow", "4th Year"))
        self.VA_section.setItemText(0, _translate("MainWindow", "A"))
        self.VA_section.setItemText(1, _translate("MainWindow", "B"))
        self.VA_roll_LE.setPlaceholderText(_translate("MainWindow", "Roll Number"))
        self.VA_view_all.setText(_translate("MainWindow", "View All"))
        self.VA_button.setText(_translate("MainWindow", "VIEW ATTENDANCE"))
        self.add_subject_label.setText(_translate("MainWindow", "ADD SUBJECT"))
        self.AS_year.setItemText(0, _translate("MainWindow", "1st Year"))
        self.AS_year.setItemText(1, _translate("MainWindow", "2nd year"))
        self.AS_year.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.AS_year.setItemText(3, _translate("MainWindow", "4th Year"))
        self.AS_button.setText(_translate("MainWindow", "ADD"))
        self.AS_section.setItemText(0, _translate("MainWindow", "A"))
        self.AS_section.setItemText(1, _translate("MainWindow", "B"))
        self.view_subject_stats_label.setText(_translate("MainWindow", "VIEW SUBJECT STATS"))
        self.VSS_year.setItemText(0, _translate("MainWindow", "1st Year"))
        self.VSS_year.setItemText(1, _translate("MainWindow", "2nd year"))
        self.VSS_year.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.VSS_year.setItemText(3, _translate("MainWindow", "4th Year"))
        self.VSS_section.setItemText(0, _translate("MainWindow", "A"))
        self.VSS_section.setItemText(1, _translate("MainWindow", "B"))
        self.VSS_button.setText(_translate("MainWindow", "VIEW STATS"))
        self.mark_attendance_label.setText(_translate("MainWindow", "MARK ATTENDANCE"))
        self.MA_year.setItemText(0, _translate("MainWindow", "1st Year"))
        self.MA_year.setItemText(1, _translate("MainWindow", "2nd Year"))
        self.MA_year.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.MA_year.setItemText(3, _translate("MainWindow", "4th Year"))
        self.MA_button.setText(_translate("MainWindow", "MARK ATTENDANCE"))
        self.MA_section.setItemText(0, _translate("MainWindow", "A"))
        self.MA_section.setItemText(1, _translate("MainWindow", "B"))
        self.SH_label.setText(_translate("MainWindow", "Subjects Handled"))
        self.signout_button.setText(_translate("MainWindow", "SIGN OUT"))

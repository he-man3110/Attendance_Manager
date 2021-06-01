# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_dashboard.ui'
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
"QPushButton#VS_view_button, QPushButton#capture_button, QPushButton#VA_button, QPushButton#ES_enroll_button,\n"
"QPushButton#sign_out_button, QPushButton#MA_mark_button, QPushButton#manage_accounts_button, QPushButton#add_subjects_button, QPushButton#drop_subjects_button, QPushButton#train_model {\n"
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
"QPushButton#VS_view_button:hover, QPushButton#capture_button:hover, QPushButton#VA_button:hover, QPushButton#ES_enroll_button:hover, QPushButton#sign_out_button:hover, QPushButton#MA_mark_button:hover,\n"
"QPushButton#manage_accounts_button:hover,QPushButton#add_subjects_button:hover, QPushButton#drop_subjects_button:hover, QPushButton#train_model:hover{\n"
"font-size: 16px;\n"
"border-top: 5px solid rgb(28, 235, 13);\n"
"border-bottom: 5px solid rgb(28, 235, 13);\n"
"border-left: 5px solid rgb(28, 235, 13);\n"
"border-right: 5px solid rgb(28, 235, 13);\n"
"}\n"
"\n"
"QPushButton#VS_view_button:pressed, QPushButton#capture_button:pressed, QPushButton#VA_button:pressed,QPushButton#ES_enroll_button:pressed,\n"
"QPushButton#sign_out_button:pressed,QPushButton#MA_mark_button:pressed,\n"
"QPushButton#manage_accounts_button:pressed,QPushButton#add_subjects_button:pressed, QPushButton#drop_subjects_button:pressed,QPushButton#train_model:pressed {\n"
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
        self.image_preview_window = QtWidgets.QLabel(self.frame)
        self.image_preview_window.setGeometry(QtCore.QRect(775, 55, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.image_preview_window.setFont(font)
        self.image_preview_window.setStyleSheet("border: 3px solid rgb(25,235,13);\n"
"border-radius: 35px;")
        self.image_preview_window.setAlignment(QtCore.Qt.AlignCenter)
        self.image_preview_window.setObjectName("image_preview_window")
        self.vline_sep = QtWidgets.QFrame(self.frame)
        self.vline_sep.setGeometry(QtCore.QRect(246, 140, 5, 561))
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
        self.view_attendance_frame.setGeometry(QtCore.QRect(277, 154, 381, 241))
        self.view_attendance_frame.setStyleSheet("")
        self.view_attendance_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.view_attendance_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.view_attendance_frame.setObjectName("view_attendance_frame")
        self.view_attendance_label = QtWidgets.QLabel(self.view_attendance_frame)
        self.view_attendance_label.setGeometry(QtCore.QRect(0, 10, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.view_attendance_label.setFont(font)
        self.view_attendance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_attendance_label.setObjectName("view_attendance_label")
        self.VA_year_cbox = QtWidgets.QComboBox(self.view_attendance_frame)
        self.VA_year_cbox.setGeometry(QtCore.QRect(20, 60, 160, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VA_year_cbox.sizePolicy().hasHeightForWidth())
        self.VA_year_cbox.setSizePolicy(sizePolicy)
        self.VA_year_cbox.setMinimumSize(QtCore.QSize(144, 51))
        self.VA_year_cbox.setMaximumSize(QtCore.QSize(160, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VA_year_cbox.setFont(font)
        self.VA_year_cbox.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VA_year_cbox.setObjectName("VA_year_cbox")
        self.VA_year_cbox.addItem("")
        self.VA_year_cbox.addItem("")
        self.VA_year_cbox.addItem("")
        self.VA_year_cbox.addItem("")
        self.VA_section = QtWidgets.QComboBox(self.view_attendance_frame)
        self.VA_section.setGeometry(QtCore.QRect(190, 60, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VA_section.setFont(font)
        self.VA_section.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VA_section.setObjectName("VA_section")
        self.VA_section.addItem("")
        self.VA_section.addItem("")
        self.VA_roll = QtWidgets.QLineEdit(self.view_attendance_frame)
        self.VA_roll.setGeometry(QtCore.QRect(20, 120, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VA_roll.setFont(font)
        self.VA_roll.setObjectName("VA_roll")
        self.VA_view_all_check = QtWidgets.QCheckBox(self.view_attendance_frame)
        self.VA_view_all_check.setGeometry(QtCore.QRect(240, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VA_view_all_check.setFont(font)
        self.VA_view_all_check.setObjectName("VA_view_all_check")
        self.VA_button = QtWidgets.QPushButton(self.view_attendance_frame)
        self.VA_button.setGeometry(QtCore.QRect(50, 180, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.VA_button.setFont(font)
        self.VA_button.setStyleSheet("")
        self.VA_button.setObjectName("VA_button")
        self.mark_attendance_frame = QtWidgets.QFrame(self.frame)
        self.mark_attendance_frame.setGeometry(QtCore.QRect(680, 410, 351, 241))
        self.mark_attendance_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mark_attendance_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mark_attendance_frame.setObjectName("mark_attendance_frame")
        self.mark_attendance_label = QtWidgets.QLabel(self.mark_attendance_frame)
        self.mark_attendance_label.setGeometry(QtCore.QRect(0, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mark_attendance_label.setFont(font)
        self.mark_attendance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mark_attendance_label.setObjectName("mark_attendance_label")
        self.MA_mark_button = QtWidgets.QPushButton(self.mark_attendance_frame)
        self.MA_mark_button.setEnabled(True)
        self.MA_mark_button.setGeometry(QtCore.QRect(30, 170, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.MA_mark_button.setFont(font)
        self.MA_mark_button.setStyleSheet("")
        self.MA_mark_button.setObjectName("MA_mark_button")
        self.MA_year = QtWidgets.QComboBox(self.mark_attendance_frame)
        self.MA_year.setGeometry(QtCore.QRect(30, 110, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MA_year.setFont(font)
        self.MA_year.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.MA_year.setObjectName("MA_year")
        self.MA_year.addItem("")
        self.MA_year.addItem("")
        self.MA_year.addItem("")
        self.MA_year.addItem("")
        self.MA_override = QtWidgets.QCheckBox(self.mark_attendance_frame)
        self.MA_override.setGeometry(QtCore.QRect(30, 60, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MA_override.setFont(font)
        self.MA_override.setObjectName("MA_override")
        self.MA_section = QtWidgets.QComboBox(self.mark_attendance_frame)
        self.MA_section.setGeometry(QtCore.QRect(190, 110, 144, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MA_section.sizePolicy().hasHeightForWidth())
        self.MA_section.setSizePolicy(sizePolicy)
        self.MA_section.setMinimumSize(QtCore.QSize(144, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MA_section.setFont(font)
        self.MA_section.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.MA_section.setObjectName("MA_section")
        self.MA_section.addItem("")
        self.MA_section.addItem("")
        self.view_subject_frame = QtWidgets.QFrame(self.frame)
        self.view_subject_frame.setGeometry(QtCore.QRect(678, 153, 351, 241))
        self.view_subject_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.view_subject_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.view_subject_frame.setObjectName("view_subject_frame")
        self.view_subject_stats_label = QtWidgets.QLabel(self.view_subject_frame)
        self.view_subject_stats_label.setGeometry(QtCore.QRect(0, 10, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.view_subject_stats_label.setFont(font)
        self.view_subject_stats_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_subject_stats_label.setObjectName("view_subject_stats_label")
        self.VS_year = QtWidgets.QComboBox(self.view_subject_frame)
        self.VS_year.setGeometry(QtCore.QRect(20, 60, 160, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VS_year.sizePolicy().hasHeightForWidth())
        self.VS_year.setSizePolicy(sizePolicy)
        self.VS_year.setMinimumSize(QtCore.QSize(144, 51))
        self.VS_year.setMaximumSize(QtCore.QSize(160, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VS_year.setFont(font)
        self.VS_year.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VS_year.setObjectName("VS_year")
        self.VS_year.addItem("")
        self.VS_year.addItem("")
        self.VS_year.addItem("")
        self.VS_year.addItem("")
        self.VS_subject = QtWidgets.QComboBox(self.view_subject_frame)
        self.VS_subject.setGeometry(QtCore.QRect(20, 120, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VS_subject.setFont(font)
        self.VS_subject.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VS_subject.setObjectName("VS_subject")
        self.VS_view_button = QtWidgets.QPushButton(self.view_subject_frame)
        self.VS_view_button.setGeometry(QtCore.QRect(40, 180, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.VS_view_button.setFont(font)
        self.VS_view_button.setStyleSheet("")
        self.VS_view_button.setObjectName("VS_view_button")
        self.VS_section = QtWidgets.QComboBox(self.view_subject_frame)
        self.VS_section.setGeometry(QtCore.QRect(190, 60, 144, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VS_section.setFont(font)
        self.VS_section.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.VS_section.setObjectName("VS_section")
        self.VS_section.addItem("")
        self.VS_section.addItem("")
        self.enroll_student_frame = QtWidgets.QFrame(self.frame)
        self.enroll_student_frame.setGeometry(QtCore.QRect(278, 410, 381, 241))
        self.enroll_student_frame.setStyleSheet("")
        self.enroll_student_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.enroll_student_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.enroll_student_frame.setObjectName("enroll_student_frame")
        self.enroll_student_label = QtWidgets.QLabel(self.enroll_student_frame)
        self.enroll_student_label.setGeometry(QtCore.QRect(10, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enroll_student_label.setFont(font)
        self.enroll_student_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enroll_student_label.setObjectName("enroll_student_label")
        self.ES_section = QtWidgets.QComboBox(self.enroll_student_frame)
        self.ES_section.setGeometry(QtCore.QRect(40, 60, 144, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_section.setFont(font)
        self.ES_section.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.ES_section.setObjectName("ES_section")
        self.ES_section.addItem("")
        self.ES_section.addItem("")
        self.ES_recursive = QtWidgets.QCheckBox(self.enroll_student_frame)
        self.ES_recursive.setGeometry(QtCore.QRect(50, 120, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_recursive.setFont(font)
        self.ES_recursive.setObjectName("ES_recursive")
        self.ES_enroll_button = QtWidgets.QPushButton(self.enroll_student_frame)
        self.ES_enroll_button.setGeometry(QtCore.QRect(40, 170, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.ES_enroll_button.setFont(font)
        self.ES_enroll_button.setStyleSheet("")
        self.ES_enroll_button.setObjectName("ES_enroll_button")
        self.ES_no_of_students = QtWidgets.QLineEdit(self.enroll_student_frame)
        self.ES_no_of_students.setGeometry(QtCore.QRect(200, 60, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ES_no_of_students.setFont(font)
        self.ES_no_of_students.setStyleSheet("padding-left:14px;")
        self.ES_no_of_students.setObjectName("ES_no_of_students")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 45, 101, 91))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("D:/Dev/Python/PyQT/AM/res/human-resources.svg"))
        self.Logo.setObjectName("Logo")
        self.sign_out_button = QtWidgets.QPushButton(self.frame)
        self.sign_out_button.setGeometry(QtCore.QRect(895, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.sign_out_button.setFont(font)
        self.sign_out_button.setStyleSheet("")
        self.sign_out_button.setObjectName("sign_out_button")
        self.manage_accounts_button = QtWidgets.QPushButton(self.frame)
        self.manage_accounts_button.setGeometry(QtCore.QRect(30, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.manage_accounts_button.setFont(font)
        self.manage_accounts_button.setStyleSheet("")
        self.manage_accounts_button.setObjectName("manage_accounts_button")
        self.add_subjects_button = QtWidgets.QPushButton(self.frame)
        self.add_subjects_button.setGeometry(QtCore.QRect(30, 260, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.add_subjects_button.setFont(font)
        self.add_subjects_button.setStyleSheet("")
        self.add_subjects_button.setObjectName("add_subjects_button")
        self.error_out = QtWidgets.QLabel(self.frame)
        self.error_out.setGeometry(QtCore.QRect(250, 650, 811, 51))
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
        self.drop_subjects_button = QtWidgets.QPushButton(self.frame)
        self.drop_subjects_button.setGeometry(QtCore.QRect(30, 340, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.drop_subjects_button.setFont(font)
        self.drop_subjects_button.setStyleSheet("")
        self.drop_subjects_button.setObjectName("drop_subjects_button")
        self.train_model = QtWidgets.QPushButton(self.frame)
        self.train_model.setGeometry(QtCore.QRect(30, 420, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.train_model.setFont(font)
        self.train_model.setStyleSheet("")
        self.train_model.setObjectName("train_model")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.close_button.setText(_translate("MainWindow", "x"))
        self.minimize_button.setText(_translate("MainWindow", "o"))
        self.drop_button.setText(_translate("MainWindow", "-"))
        self.AM_main_label.setText(_translate("MainWindow", "ATTENDANCE MANAGER"))
        self.disp_username_label.setText(_translate("MainWindow", "USERNAME"))
        self.image_preview_window.setText(_translate("MainWindow", "No Preview"))
        self.view_attendance_label.setText(_translate("MainWindow", "VIEW ATTENDANCE"))
        self.VA_year_cbox.setItemText(0, _translate("MainWindow", "1st Year"))
        self.VA_year_cbox.setItemText(1, _translate("MainWindow", "2nd year"))
        self.VA_year_cbox.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.VA_year_cbox.setItemText(3, _translate("MainWindow", "4th Year"))
        self.VA_section.setItemText(0, _translate("MainWindow", "A"))
        self.VA_section.setItemText(1, _translate("MainWindow", "B"))
        self.VA_roll.setPlaceholderText(_translate("MainWindow", "Roll Number"))
        self.VA_view_all_check.setText(_translate("MainWindow", "View All"))
        self.VA_button.setText(_translate("MainWindow", "VIEW ATTENDANCE"))
        self.mark_attendance_label.setText(_translate("MainWindow", "MARK ATTENDANCE"))
        self.MA_mark_button.setText(_translate("MainWindow", "MARK"))
        self.MA_year.setItemText(0, _translate("MainWindow", "1st Year"))
        self.MA_year.setItemText(1, _translate("MainWindow", "2nd Year"))
        self.MA_year.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.MA_year.setItemText(3, _translate("MainWindow", "4th Year"))
        self.MA_override.setText(_translate("MainWindow", "OVERRIDE SCHEDULE"))
        self.MA_section.setItemText(0, _translate("MainWindow", "A"))
        self.MA_section.setItemText(1, _translate("MainWindow", "B"))
        self.view_subject_stats_label.setText(_translate("MainWindow", "VIEW SUBJECT STATS"))
        self.VS_year.setItemText(0, _translate("MainWindow", "1st Year"))
        self.VS_year.setItemText(1, _translate("MainWindow", "2nd year"))
        self.VS_year.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.VS_year.setItemText(3, _translate("MainWindow", "4th Year"))
        self.VS_view_button.setText(_translate("MainWindow", "VIEW STATS"))
        self.VS_section.setItemText(0, _translate("MainWindow", "A"))
        self.VS_section.setItemText(1, _translate("MainWindow", "B"))
        self.enroll_student_label.setText(_translate("MainWindow", "ENROLL STUDENT"))
        self.ES_section.setItemText(0, _translate("MainWindow", "A"))
        self.ES_section.setItemText(1, _translate("MainWindow", "B"))
        self.ES_recursive.setText(_translate("MainWindow", "RECURSIVE"))
        self.ES_enroll_button.setText(_translate("MainWindow", "ENROLL"))
        self.ES_no_of_students.setPlaceholderText(_translate("MainWindow", "No. of Students"))
        self.sign_out_button.setText(_translate("MainWindow", "SIGN OUT"))
        self.manage_accounts_button.setText(_translate("MainWindow", "MANAGE ACCOUNTS"))
        self.add_subjects_button.setText(_translate("MainWindow", "ADD SUBJECT"))
        self.drop_subjects_button.setText(_translate("MainWindow", "DROP SUBJECT"))
        self.train_model.setText(_translate("MainWindow", "TRAIN MODEL"))

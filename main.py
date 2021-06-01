import sys
import platform
import time
import cv2
import os
import re

from PySide2 import QtCore
from PySide2.QtCore import QEvent, QRegExp, Qt, QTimer, QRect
from PySide2.QtWidgets import *
from PySide2.QtGui import QColor, QPixmap, QRegExpValidator, QImage, QWindow, QBrush, QPainter
from PySide2.QtWidgets import QMainWindow

#"D:/Dev/Python/PyQT/AM/res/human-resources.svg"

import admin_dashboard
import landing_page
import login_page
import signup_page
import user_dashboard
import enroll_student
import video_feed_display
import manage_accounts
import add_sub_pop
import drop_sub_pop
import config_pop
import error_out
import vault
import settings
import image_io

IMG_COUNT = 2
TEMP_GLOB_PATH = 'D:/Dev/Python/PyQT/AM/known/'
ADMIN_MODE = 1
USER_MODE = 0
ENROLL = 10
SURVAL = 20
NO_CONTEXT = 30

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set all the main display properties
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        #Timers
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.msg_timer = QTimer()
        self.msg_timer.timeout.connect(self.update_message)
        self.shutter = QTimer()
        self.shutter.timeout.connect(self.capture)



        #camera
        self.cap_device = cv2.VideoCapture(0)

        # UI Pages initialized here
        self.landing_page = landing_page.Ui_MainWindow()
        self.sign_in_page = login_page.Ui_MainWindow()
        self.sign_up_page = signup_page.Ui_MainWindow()
        self.dashboard_admin = admin_dashboard.Ui_MainWindow()
        self.dashboard_user = user_dashboard.Ui_MainWindow()
        self._enroll_student = enroll_student.Ui_MainWindow()
        self.video_preview_window = video_feed_display.Ui_MainWindow()
        self.current_dialog = None
        
        # Runtime Helper Variables
        self.mode = ADMIN_MODE #change this to 0
        self.user_name = "H E M A N ⚡"
        self.login_id_string = ""
        self.login_password = ""
        self.year = ""
        self.section = ""
        self.subject = ""       
        self.captured_image = ""
        self.profile_image = ""
        self.dev = self._resize_img("Admin.jpg", "jpg")#"D:/Dev/Python/PyQT/AM/res/Admin.jpg", "jpg")
        self.error_message = "If you see this then the software has a BUG!"
        self.context = NO_CONTEXT
        self.capture_count = 10
        self.sessionActive = False  
        self.cap_imgs = []
        self.count = 0
        self.mcount = 0
        self.sec = 0
        #Start Up Actions
        #self.sec = settings._init_()
        self._load_landing_page()

#Check thiss
    def _load_landing_page(self):
        self.landing_page.setupUi(self)
        self.landing_page.sign_in_button.clicked.connect(self._load_sign_in_page)
        self.landing_page.sign_up_button.clicked.connect(self._load_sign_up_page)
        self.landing_page.set_config.clicked.connect(self._load_config_dialog)
        self._set_controls(self.landing_page)
        if self.sec != 0:
            self.landing_page.error_out.setText(error_out.ErrorOut(self.sec))
        self.show()

    def _load_sign_in_page(self):
        self.sign_in_page.setupUi(self)
        self.mode = ADMIN_MODE #change this to 0
        self.sign_in_page.login_button.clicked.connect(self.start_session)
        self.sign_in_page.back_button.clicked.connect(self.end_session)
        self.sign_in_page.username_LE.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z0-9.]*\@[a-zA-Z0-9.]*"), self))
        self._set_controls(self.sign_in_page)  
        self.show()
    
    def _load_sign_up_page(self):
        self.sign_up_page.setupUi(self)
        self.mode = 3110
        self.sign_up_page.signup_button.clicked.connect(self.get_sign_up_details)
        self.sign_up_page.back_button.clicked.connect(self._load_landing_page)

        self.sign_up_page.Phone_LE.setValidator(QRegExpValidator(QRegExp(r"[0-9]{10}"), self))
        self.sign_up_page.FirstName_LE.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z ]*"), self))
        self.sign_up_page.byear_LE.setValidator(QRegExpValidator(QRegExp(r"[0-9]{4}"), self))
        self.sign_up_page.Email_LE.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z0-9.]*\@[a-zA-Z0-9.]*"), self))

        self._set_controls(self.sign_up_page)
        self.show()
    
    def _load_enroll_page(self):
        self.context = ENROLL
        self._enroll_student.setupUi(self)
        self.startCamera()
        self._enroll_student.Uname_display.setText(self.user_name)
        self._enroll_student.capture_button.clicked.connect(self.capture_image)
        self._enroll_student.enroll_button.clicked.connect(self._collect_enrollment_data)
        self._enroll_student.back_button.clicked.connect(self.moveBack)
        self._enroll_student.dp.setPixmap(self.dev)
        self._enroll_student.ES_Phone_LE.setValidator(QRegExpValidator(QRegExp(r"[0-9]{10}"), self))
        self._enroll_student.ES_FirstName_LE.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z ]"), self))
        self._enroll_student.ES_byear_LE.setValidator(QRegExpValidator(QRegExp(r"[0-9]{4}"), self))
        self._enroll_student.ES_Email_LE.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z0-9.]*\@[a-zA-Z0-9.]*"), self))
        self._set_controls_enroll()
        self.show()

    def _load_dashboard(self):
        if self.mode == ADMIN_MODE:
            self.dashboard_admin.setupUi(self)
            self.dashboard_admin.sign_out_button.clicked.connect(self._load_landing_page)
            self.dashboard_admin.ES_enroll_button.clicked.connect(self._load_enroll_page)
            self.dashboard_admin.MA_mark_button.clicked.connect(self._load_video_preview)
            self.dashboard_admin.manage_accounts_button.clicked.connect(self._load_manage_dialog)
            self.dashboard_admin.add_subjects_button.clicked.connect(self._load_add_dialog)
            self.dashboard_admin.drop_subjects_button.clicked.connect(self._load_drop_dialog)
            
            self.dashboard_admin.disp_username_label.setText(self.user_name)
            self.dashboard_admin.image_preview_window.setPixmap(self.dev)
            self._set_controls(self.dashboard_admin)
            self.show()

        elif self.mode == USER_MODE:
            self.dashboard_user.setupUi(self)
            self._setup_dashboard_user()

            self.dashboard_user.signout_button.clicked.connect(self._load_landing_page)
            self.dashboard_user.MA_button.clicked.connect(self._load_video_preview)
            self.dashboard_user.AS_button.clicked.connect(self._subscribe_subject)


            self._set_controls(self.dashboard_user)
            self.show()
        else:
            self.sign_in_page.error_out.settext(error_out.ErrorOut(7))

    def _load_video_preview(self):
        if self.mode == ADMIN_MODE:
            self.year = self.dashboard_admin.MA_year.currentText()
            self.year = re.search(r"([0-9])", self.year).group(1)
            self.section = self.dashboard_admin.MA_section.currentText()
            self.subject = "python"#self.dashboard_admin.MA_subject.currentText()
        self.context = SURVAL
        self.sessionActive = True
        self.startCamera()
        self.error_message = "Capturing Images"
        self.startMtimer()
        self.video_preview_window.setupUi(self)
        self.video_preview_window.stop_button.clicked.connect(self.moveBack)
        self.video_preview_window.close_button.clicked.connect(self.stopCamera)
        self.video_preview_window.disp_username_label.setText(self.user_name)
        self._set_controls(self.video_preview_window)
        self.show()

    def _load_manage_dialog(self, checked):
        dlg = manage_accounts.Ui_Dialog()
        self.current_dialog = dlg
        dlg.setWindowModality(QtCore.Qt.ApplicationModal)
        dlg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        dlg.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        dlg.setupUi(dlg)
        dlg.close_button.clicked.connect(self.__dialog_close)
        dlg.drop_button.clicked.connect(dlg.showMinimized)
        dlg.show()
        if dlg.exec_():
            pass

    def _load_add_dialog(self, checked):
        dlg = add_sub_pop.Ui_Dialog()
        self.current_dialog = dlg
        dlg.setWindowModality(QtCore.Qt.ApplicationModal)
        dlg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        dlg.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        dlg.setupUi(dlg)
        dlg.close_button.clicked.connect(self.__dialog_close)
        dlg.drop_button.clicked.connect(dlg.showMinimized)
        dlg.show()
        if dlg.exec_():
            pass

    def _load_drop_dialog(self, checked):
        dlg = drop_sub_pop.Ui_Dialog()
        self.current_dialog = dlg
        dlg.setWindowModality(QtCore.Qt.ApplicationModal)
        dlg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        dlg.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        dlg.setupUi(dlg)
        dlg.close_button.clicked.connect(self.__dialog_close)
        dlg.drop_button.clicked.connect(dlg.showMinimized)
        dlg.show()
        if dlg.exec_():
            pass

    def _load_config_dialog(self, checked):
        dlg = config_pop.Ui_Dialog()
        self.current_dialog = dlg
        dlg.setWindowModality(QtCore.Qt.ApplicationModal)
        dlg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        dlg.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        dlg.setupUi(dlg)
        dbun,dbp,dbip,dbpt,dbu,dbs = settings._get_config_details()
        dlg.db_username.setText(dbun)
        dlg.db_password.setText(str(dbp))
        dlg.utb_name.setText(dbu)
        dlg.stb_name.setText(dbs)
        dlg.db_ip.setText(str(dbip))
        dlg.db_port.setText(str(dbpt))
        dlg.drop.clicked.connect(self._close_config_dialog)
        dlg.close_button.clicked.connect(self.__dialog_close)
        dlg.drop_button.clicked.connect(dlg.showMinimized)
        dlg.show()
        if dlg.exec_():
            pass

#Validation to be added here
    def _close_config_dialog(self):
        #Add input data validation here
        error_code = settings._update_config_details(
            self.current_dialog.db_username.text(),
            self.current_dialog.db_password.text(),
            self.current_dialog.db_ip.text(),
            self.current_dialog.db_port.text(),
            self.current_dialog.utb_name.text(),
            self.current_dialog.stb_name.text()
        )
        if error_code != 0:
            self.current_dialog.error_out.setText(error_out.ErrorOut(error_code))
        else:
            self.landing_page.setErrorContextColor("rgb(25,235,13)")
            self.landing_page.error_out.setText("Changes Saved sucessfully!")
            self.current_dialog.close()
            self.current_dialog = None
        
    def get_sign_up_details(self):
        self.sign_up_page.red_error_init()
        name = self.sign_up_page.FirstName_LE.text() + " " + self.sign_up_page.LastName_LE.text()
        email = self.sign_up_page.Email_LE.text()
        phone = self.sign_up_page.Phone_LE.text()
        password = self.sign_up_page.Password_LE.text()
        year = self.sign_up_page.byear_LE.text()
        isadmin = 0
        if self.sign_up_page.make_admin_checkbox.isChecked():
            isadmin = 1
        if password != self.sign_up_page.cpassword_LE.text():
            self.sign_up_page.error_out.setText("Passwords do not match!")
            return
        elif len(name) == 0 or len(email) == 0 or len(phone) == 0 or len(year) == 0:
            self.sign_up_page.error_out.setText("Enter all the details!!")
            return
        elif len(password) < 8:
            self.sign_up_page.error_out.setText("Password should have atleast 8 characters")
            return
        else:
            dob = []
            dob.append(int(self.sign_up_page.bday_comboBox.currentText()))
            dob.append(self.sign_up_page.bmonth_comboBox.currentText())
            dob.append(int(year))
            error_code = vault.add_user(name, email, phone, password, dob, isadmin)
            if error_code != 0:
                self.sign_up_page.error_out.setText(error_out.ErrorOut(error_code))
                return
        self.sign_up_page.green_error_init()
        self.sign_up_page.error_out.setText("Account created successfully!")
        #self._load_landing_page()

    def start_session(self):
        uname = self.sign_in_page.username_LE.text()
        passwd = self.sign_in_page.password_LE.text()
        if len(uname) == 0 or len(passwd) == 0:
            self.sign_in_page.error_out.setText("Please fill the required field!")
            return
        error_code, self.mode, self.user_name = vault.grant_permission(uname, passwd)
        if error_code == 0:
            self.sign_in_page.error_out.setText("")
            self._load_dashboard()
        else:
            self.sign_in_page.error_out.setText(error_out.ErrorOut(error_code))

    def end_session(self):
        self.mode = 0
        self.user_name = "HEMAN"
        self._load_landing_page()

    def viewCam(self):
        ret, image = self.cap_device.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.sessionActive:
            if self.capture_count > 0 and self.count%180 == 0:
                self.cap_imgs.append(image)
                self.capture_count -= 1
            self.count += 1
            if self.capture_count == 0:
                self.error_message = "Running facial recognition"
                self.sessionActive = False
                self.count = 0
                self.update_list()
                self.moveBack()

        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        if self.context == ENROLL:
            self._enroll_student.display.setPixmap(QPixmap.fromImage(qImg))
        elif self.context == SURVAL:
            self.video_preview_window.video_out.setPixmap(QPixmap.fromImage(qImg))
        else:
            pass

    def startCamera(self):
        if not self.timer.isActive():
            self.cap_device = cv2.VideoCapture(0)
            self.timer.start(30)
    
    def stopCamera(self, close_window=True):
        if self.timer.isActive():
            self.timer.stop()
            self.cap_device.release()
            self.context = NO_CONTEXT
        if close_window:
            self.close()

    def startShutter(self):
        if not self.shutter.isActive():
            self.shutter.start(1000)

    def capture(self):
        self.shutter.stop()
        self.msg_timer.stop()
        self.capture_duration = 10
        self.shutter_press = False
        self.error_message = "Running Face Recognition"
        self.msg_timer.start(500)
        self.update_list()

    def startMtimer(self):
        if not self.msg_timer.isActive():
            self.msg_timer.start(500)

    def update_message(self):
        self.video_preview_window.error_out.setText(self.error_message + "."*self.mcount)
        self.mcount += 1
        if self.mcount > 3:
            self.mcount = 0

    def moveBack(self):
        if self.timer.isActive():
            self.timer.stop()
            self.cap_device.release()
            if self.msg_timer.isActive():
                self.msg_timer.stop()
            self.video_preview_window.cButtoname("BACK")
            self.video_preview_window.error_out.setText("Processing")
            
            #call the vault function that starts the recognition engine and returns the list of names
            #vault.mark_attendance()
            
            self.video_preview_window.error_out.setText("Finished!")
            #update the recognized faces here.
            flst = ["Hemanth" , "Ashok", "Vinay", "Yukta", "Rohan", "Shamanth", "Suhas", "Suresh", "Vasquez", "Aerielle", "Casper the ghost", "Jhonty", "Mark", "Susan"] 
            #flst = vault.get_identified_list()
            for name in flst:
               self.video_preview_window.add_label(name)
        else:
            self._load_dashboard()

    def update_list(self):
        error_code, retlst = 0, []#vault.mark_attendance(self.cap_imgs, self.year, self.section, self.subject)
        for image in self.cap_imgs:
            cv2.imshow("Captured Images", image)
            cv2.waitKey(0)
        cv2.destroyAllWindows()
        if error_code != 0:
            self.video_preview_window.error_out.setText(error_out.ErrorOut(error_code))
            time.sleep(2)
            #Go back
        else:
            #call the scroll area function to add names to the list
            pass

    def capture_image(self, event):
        global TEMP_GLOB_PATH 
        retval, image = self.cap_device.read()
        self.stopCamera(False)
        time.sleep(1)
        cv2.imwrite(os.path.join(TEMP_GLOB_PATH, 'opencv'+str(IMG_COUNT)+'.jpeg'), image)
        self.captured_image = TEMP_GLOB_PATH + 'opencv/' + str(IMG_COUNT) + '.jpeg'
        display_obj = QPixmap("D:/Dev/Python/PyQT/AM/known/opencv2.jpeg")
        self._enroll_student.image_preview_window.setPixmap(display_obj)

    def _resize_img(imgpath, imgtype="jpg", size=64):
        # Load image
        imgdata = open("Admin.jpg", 'rb').read()
        image = QImage.fromData(imgdata, imgtype)
  
        # convert image to 32-bit ARGB (adds an alpha
        # channel ie transparency factor):
        image.convertToFormat(QImage.Format_ARGB32)
  
        # Crop image to a square:
        imgsize = min(image.width(), image.height())
        rect = QRect(
            (image.width() - imgsize) / 2,
            (image.height() - imgsize) / 2,
            imgsize,
            imgsize,
        )
       
        image = image.copy(rect)
  
        # Create the output image with the same dimensions 
        # and an alpha channel and make it completely transparent:
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)
  
        # Create a texture brush and paint a circle 
        # with the original image onto the output image:
        brush = QBrush(image)
  
        # Paint the output image
        painter = QPainter(out_img)
        painter.setBrush(brush)
  
        # Don't draw an outline
        painter.setPen(Qt.NoPen)
  
        # drawing circle
        painter.drawEllipse(0, 0, imgsize, imgsize)
  
        # closing painter event
        painter.end()
  
        # Convert the image to a pixmap and rescale it. 
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size = 64 * pr
        pm = pm.scaled(size, size, Qt.KeepAspectRatio, 
                               Qt.SmoothTransformation)
  
        # return back the pixmap data
        return pm

    def __test(self):
        pass

    def _collect_enrollment_data(self):
        if len(self.captured_image) <= 0:
                self._enroll_student.error_out.setText(error_out.ErrorOut(12))
        else:    
            name = self._enroll_student.ES_FirstName_LE.text() + " " + self._enroll_student.ES_LastName_LE.text()
            email = self._enroll_student.ES_Email_LE.text()
            phone = self._enroll_student.ES_Phone_LE.text()
            blood_type = self._enroll_student.ES_blood_comboBox.currentText() 
            roll = self._enroll_student.ES_roll_LE.text()
            byear = int(self._enroll_student.ES_byear_LE.text())
            bday = int(self._enroll_student.ES_bday.currentText())
            bmonth = self._enroll_student.ES_bmonth.currentText()
            year = self._enroll_student.ES_year_comboBox.currentText()    
            error_code = 1#vault.save(name, email, phone, blood_type, year, roll, bday, bmonth, byear, self.captured_image)
            if error_code != 0:
                self._enroll_student.error_out.setText(error_out.ErrorOut(error_code))
                return

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #error here
    def _subscribe_subject(self):
        subname = self.dashboard_user.AS_subject_list.currentText()
        section = self.dashboard_user.AS_section.currentText()
        year = self.dashboard_user.AS_Year.text() #Take care of converting this
        if len(year) == 0 or len(subname) == 0:
            self.dashboard_user.error_out.setText(error_out.ErrorOut(16))
            return 
        else:
            error_code = 0#vault.add_subject(self.user_name.replace(" ", "_").lower(),subname, year, section)
            if error_code != 0:
                self.dashboard_user.error_out.setText(error_out.ErrorOut(error_code))
            else: # Fix Bug Here
                self.dashboard_user.SH_1.setText(subname)

    def _setup_dashboard_user(self):
        self.dashboard_user.disp_username_label.setText(self.user_name)
        error_code, sublst = vault.get_subjects(self.user_name)
        if error_code != 0:
            self.dashboard_user.error_out.setText(error_out.ErrorOut(error_code))
        else:
            for subject in sublst:
                self.dashboard_user.MA_subject_list.addItem(subject)

    def _set_controls(self, page):
        #page.frame.setGraphicsEffect(self.shadow)
        page.top_bar.mouseMoveEvent = self.moveWindow
        page.close_button.clicked.connect(lambda: self.close())
        page.drop_button.clicked.connect(lambda: self.showMinimized())
        
    def _set_controls_enroll(self):
        self._enroll_student.frame.setGraphicsEffect(self.shadow)
        self._enroll_student.top_bar.mouseMoveEvent = self.moveWindow
        self._enroll_student.close_button.clicked.connect(lambda : self.stopCamera())
        self._enroll_student.drop_button.clicked.connect(lambda : self.showMinimized())

    def __dialog_close(self):
        self.current_dialog.close()
        self.current_dialog = None

    def test(self):
        pass

if __name__ == "__main__":
    App = QApplication(sys.argv)
    app = MainWindow()
    app.show()
    sys.exit(App.exec_())
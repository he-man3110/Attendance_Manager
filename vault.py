import os
import cv2
import datetime
import mysql.connector
from hashlib import sha1
import  recognition_engine
import settings

UNAME = 'OMENX'
PASSWORD = '3110'
HOST_IP = '127.0.0.1'
RESOLUTION_LEVEL = 100

BASE_DIR = "D:/Dev/Python/PyQT/AM/"
TRAINING_IMAGES = "D:/Dev/Python/PyQT/AM/images/"
TEMPORARY_MEM_DUMP = "D:/Dev/Python/PyQT/AM/unknown"

NAME_SET = set()
COUNT = 0

__mconv = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}

def _connect_mysql(database_name=""):
    global UNAME
    global PASSWORD
    global HOST_IP
    if database_name != "":
        conn = mysql.connector.connect(
            user=UNAME, password=PASSWORD, host=HOST_IP, database=database_name)
    else:
        conn = mysql.connector.connect(
            user=UNAME, password=PASSWORD, host=HOST_IP)
    conn.autocommit = True
    return conn

def add_subject(username, subject_name, year, section):
    conn = _connect_mysql("learning")
    cursor = conn.cursor()
    try:
        sqlcmd = f"""INSERT INTO {username}(Subject, Year, section)
                     VALUES ('{subject_name}', '{year}', '{section}');"""
        cursor.execute(sqlcmd)
        conn.commit()
        return 0
    except :
        print("Error occurred while adding the subject!")
        return 11
    try:
        sqlcmd = f"""CREATE TABLE {subject_name.replace(" ", "_").lower()}(RollId varchar(12) primary key, Name varchar(50));"""
        
        #Subscribe students to the course


    except:
        print("Error while creating subject db")
        return 

def drop_subject(username, subject_name=""):
    conn = _connect_mysql("learning")
    cursor = conn.cursor()
    if len(subject_name) > 0:
        try:
            sqlcmd = f"""DELETE FROM {username} WHERE Subject='{subject_name}';"""
            cursor.execute(sqlcmd)
            conn.commit()
            return 0
        except:
            print("Specified subject does not exist")
            return 14
    else:
        try:
            sqlcmd = f"""TRUNCATE TABLE {username};"""
            cursor.execute(sqlcmd)
            conn.commit()
            return 0
        except:
            print("Error occured while dropping the subject")
            return 13

def get_subjects(username : str) -> list:
    conn = _connect_mysql("learning")
    cursor = conn.cursor()
    retlst = []
    try:
        sqlcmd = f"""SELECT Subject FROM {username.replace(" ", "_").lower()};"""
        cursor.execute(sqlcmd)
        #get the results and convert it into a list
        lst = cursor.fetchall()
        retlst = []
        for item in lst:
            retlst.append(str(item[0]))
        return 0, retlst
    except :
        print("Error occured while loading your info :(")
        return 15, []

def train(year, section ,subject):
    recognition_engine.KNOWN_FACES_DIR = BASE_DIR + "images/" + str(year + "/") + str(section + "/") + str(subject + "/")
    recognition_engine.MODEL_NAME = "FS_" + str(year) + str(section) 
    #recognition_engine.REVISION = str(version)
    recognition_engine.recognize(True)
    pass

#check sql
def _make_unique(rollst : list):
    global NAME_SET
    global COUNT
    retval = []
    conn = _connect_mysql("learning")
    cursor = conn.cursor()
    for roll in rollst:
        try:
            sqlcmd = f"""SELECT FullName FROM am_student_accounts WHERE Rollid='{roll}';"""
            cursor.execute(sqlcmd)
            name = cursor.fetchone()
            try:
                if COUNT > 0:
                    if name in NAME_SET:
                        continue
                    else:
                        retval.append(name)
                else:
                    NAME_SET.add(name)
            except:
                print("error")
                continue
        except:
            continue
    if COUNT == 0:
        COUNT += 1
        return list(NAME_SET)
    else:
        COUNT += 1
        return retval

#check working
def mark_attendance(image_list, year, section, subject):
    # load the exsisting model to recognize
    recognition_engine.MODEL_NAME = "FS_" + str(year) + str(section)
    #recognition_engine.REVISION = str(version)
    roll_lst = recognition_engine.recognize()
    name_lst = _make_unique(roll_lst)

    conn = _connect_mysql("learning")
    cursor = conn.cursor()
    currentDate = str(datetime.date.today()).replace("-","_")
    if True: #Add a check to see if column with today's date has already been created or not.
        try:
            sqlcmd = f"""ALTER TABLE {subject} ADD COLUMN {currentDate} int;"""
            cursor.execute(sqlcmd)
            conn.commit()
        except:
            print("Error while storing attendance!")
            return 17
    for roll in roll_lst:
        try:
            sqlcmd = f"""UPDATE {subject} SET {currentDate} = {currentDate} + 1 WHERE Rollid='{roll}';"""
            cursor.execute(sqlcmd)
            conn.commit()
        except:
            #Write error log
            continue
    return 0, name_lst



def get_name_from_roll(roll):
    pass

#check
def _save_image(images : list, roll : str, year : str, section : str) -> bool:
    cwdirec = TRAINING_IMAGES + str(year + "/") + str(section + "/") + str(roll)
    count = 0
    try:
        os.chdir(cwdirec)
        count = os.listdir(cwdirec) + 1
    except FileNotFoundError as e:
        print("No existing directory found!\nCreating a new one....")
        os.mkdir(cwdirec)
        count = 1
    for image in images:
        try:
            cv2.imwrite(str(count)+".jpg", image, [cv2.IMWRITE_JPEG_QUALITY, RESOLUTION_LEVEL])
        except:
            return False
    return True

def create_database():
    conn = _connect_mysql()

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing query to create a database
    sql = ''' CREATE database {} '''.format(input("Database Name : "))

    # Creating a database
    cursor.execute(sql)
    print("Database created successfully..!")

    # Closing the connection
    conn.close()

def check(val, cid, conn, table=""):
    cursor = conn.cursor()
    if len(table) == 0:
        return None
    if cid == "email":
        try:  
            sqlcmd = f"""SELECT COUNT(*) FROM {table} WHERE Email='{val}';"""
            cursor.execute(sqlcmd)
            retstat = cursor.fetchone()
            if retstat[0] == 0:
                return False
            elif retstat[0] > 0:
                return True
            else:
                return None
        except:
            conn.rollback()
            print("Some error occured while checking")
            return None
    elif cid == "roll":
        try:
            sqlcmd = f"""SELECT COUNT(*) FROM {table} WHERE rollid='{val}';"""
            cursor.execute(sqlcmd)
            retstat = cursor.fetchone()
            if retstat[0] == 0: 
                return False
            else:
                return True
        except:
            conn.rollback()
            print("Some error occured while checking")
            return None
    else:   
        print("Invalid cid!")

def grant_permission(email, password):
    conn = _connect_mysql("learning")
    cursor = conn.cursor()

    _exists = check(email, "email", conn, "am_user_accounts")
    if _exists:
        _hashed = sha1(str(password).encode("utf-8")).hexdigest()
        sqlcmd = f"""SELECT Phash, isAdmin, UserName FROM am_user_accounts WHERE Email='{email}';"""
        cursor.execute(sqlcmd)
        result = cursor.fetchone()
        if result[0] == _hashed:
            return [0, result[1], result[2]] 
        else:
            return [8, 0, ""]
    else:
        return [7, 0, ""]

#check and upate params
def add_user(name, email, phone, password, dob, isadmin):
    conn = _connect_mysql("learning")
    cursor = conn.cursor()
    dob = _conv(dob[0], dob[1], dob[2])
    _exists = check(email, "email", conn, "am_user_accounts")
    if _exists:
        return 2
    _hashed = sha1(str(password).encode("utf-8")).hexdigest()
    print(_hashed)
    try:
        sqlcmd = f"""INSERT INTO am_user_accounts(UserName, Email, Phone, Phash, dob, isAdmin)
                    VALUES ('{name}', '{email}', {phone}, '{_hashed}', '{dob}', '{isadmin}');"""
        cursor.execute(sqlcmd)
        conn.commit()

        #Create user table to store their subjects
        sqlcmd2 = f"""CREATE TABLE {name}(Subject varchar(30), Year varchar(1), section varchar(1));"""
        cursor.execute(sqlcmd2)
        conn.commit()
        return 0
    except:
        conn.rollback()
        print("Error occured while creating account!")
        return 6


def save(uname, email, phone, blood_type, syear, roll, bday, bmonth, byear, section, candidate_image):
    conn = _connect_mysql("learning")
    cursor = conn.cursor()
    #check if the email exists
    _exists = check(email, "email", conn, "am_student_accounts")
    if _exists:
        return 2
    #check if the roll number exists
    _exists = check(roll, "roll", conn, "am_student_accounts")
    if _exists:
        return 3
    dob = _conv(bday, bmonth, byear)
    imlst = []
    imlst.append(candidate_image)
    _check = _save_image(imlst, roll)
    if not _check:
        return 10
    # create a new row in accounts table
    try:
        sqlcmd = f"""INSERT INTO am_student_accounts(Rollid, FullName, Email, Phone, dob, Study_year, Btype, section)
                    VALUES ('{roll}', '{uname}', '{email}', '{phone}', '{dob}', '{syear}', '{blood_type}', '{section}');"""
        cursor.execute(sqlcmd)
        conn.commit()
        return 0
    except:
        conn.rollback()
        return 9

def _conv(day, month, year):
    global __mconv
    return str(day) + "-" + str(__mconv[month.lower()]) + "-" + str(year)

def test():
    _make_unique(["Hemanth", "hemanth", "Rahul"])
    _make_unique(["Hemanth", "nishanth"])
    print(NAME_SET)


if __name__=='__main__':
    #objjj = sha1("Hemanth".encode("utf-8"))
    #print(objjj.hexdigest())
    #print(add_user("Sachin T S", "suhsasts19@gmail.com", "7976626240", "passmein", [19, "july", 1999], 0))
    #print(check("suhasts19@gmail.com", "email", _connect_mysql("learning"), "am_user_accounts"))
    #print(grant_permission("hemanthmbb@gmail.com", "Hemanth"))
    #print(save("Suhas T S", "suhasts19@gmail.com", "9742529571", "B+", "4", "4BD16EC068", 19, "july", 1999))
    #print(os.listdir(TRAINING_IMAGES))
    #print(os.chdir(TRAINING_IMAGES + "4BD17EC09"))
    #print(os.listdir(TRAINING_IMAGES + "4BD17EC029"))
    #func()
    #print(get_subjects("Hemanth M B"))
    pass
from io import FileIO
import json
import datetime
import mysql

DB_USERNAME = 'OMENX'
DB_PASSWORD = '3110'
HOST_IP = '127.0.0.1'
PORT = 3306
RESOLUTION_LEVEL = 100
CONFIG_FILE_NAME = "config.json"

MODEL_NAME = "FSXH_v"
EXTENSION = ".skull" 

#json Variables
SUBJECT = "subjects"
MODEL_INFO = "skull_version"
CURRDATE = "main_date"
DB_NAME = "DATABASE_NAME"
USTB = "USER_TABLE"
STTB = "STUDENT_MAIN_TABLE"
DBUN = "DATABASE_USERNAME"
DBPW = "DATABASE_PASSWORD"
DBIP = "HOST_IP"
DBPT = "PORT"

def _connect_mysql(database_name=""):
    global DB_USERNAME
    global DB_PASSWORD
    global HOST_IP
    if database_name != "":
        conn = mysql.connector.connect(
            user=DB_USERNAME, password=DB_PASSWORD, host=HOST_IP, database=database_name)
    else:
        conn = mysql.connector.connect(
            user=DB_USERNAME, password=DB_PASSWORD, host=HOST_IP)
    conn.autocommit = True
    return conn

def _load_config_file(mode : str = "r+"):
    fhandle = open("config.json", "r+")
    return fhandle, json.loads(fhandle.read())

def _save_config_file(data : dict, file : FileIO, close : bool = False) -> int:
    try:
        file.seek(0)
        json.dump(data, file)
        file.truncate()
        if close:
            file.close()
        return 0
    except:
        return 19
#Full functionality disabled
def _init_() -> int:
    global CURRDATE
    global DB_USERNAME
    global DB_PASSWORD
    global HOST_IP
    global PORT

    file_handle, d_config = _load_config_file()
    d_config[CURRDATE] = str(datetime.date.today())
    DB_USERNAME = d_config[DBUN]
    DB_PASSWORD = d_config[DBPW]
    HOST_IP = d_config[DBIP]
    PORT = d_config[DBPT] 

    if d_config["unboxed"] == False:
        d_config["unboxed"] = True
        #create all the database required
        #return __initialize_db()   
    for subname in d_config[SUBJECT]:
        d_config[SUBJECT][subname]["marked"] = False
        d_config[SUBJECT][subname]["current_date"] = d_config[CURRDATE]
    return _save_config_file(d_config, file_handle, True)
#Has to be checked
def __initialize_db() -> int:
    global DB_NAME
    global STTB
    file_handle, d_config = _load_config_file("r")
    file_handle.close()
    conn = _connect_mysql(d_config[DB_NAME])
    cursor = conn.cursor()
    try:
        sqlcmd = f"""CREATE TABLE {d_config[USTB]}(UserName varchar(30), Email varchar(30), 
                    Phone INT, Phash varchar(35), dob varchar(12), isAdmin BOOLEAN);"""
        cursor.execute(sqlcmd)
        conn.commit()
    except:
        return 18
    try:
        sqlcmd = f"""CREATE TABLE {d_config[STTB]}(Rollid varchar(10) unique not null primary key, FullName varchar(50), Email varchar(30), 
	                Phone varchar(10), dob varchar(12),  Study_year varchar(5), Btype varchar(4), Section varchar(2));"""
    except:
        return 18
    return 0

def is_marked(subject : str) -> bool:
    f = open(CONFIG_FILE_NAME, 'r')
    info = json.loads(f.read())
    f.close()
    return info[SUBJECT][subject]["marked"]

def revise_model_name(year : int, section : str) -> str:
    file_handle, d_config = _load_config_file()
    base_name = d_config[MODEL_INFO][str(year)][section]["base_name"]
    current_revision = d_config[MODEL_INFO][str(year)][section]["revision"]
    new_revision = current_revision + 1.0
    d_config[MODEL_INFO][str(year)][section]["revision"] = new_revision
    d_config[MODEL_INFO][str(year)][section]["last_trained"] = str(datetime.date.today())
    _save_config_file(d_config, file_handle, True)
    return str(base_name) + str(new_revision) + str(EXTENSION)

def _get_config_details() -> list:
    file_handle, d_config = _load_config_file()
    file_handle.close()
    return [d_config[DBUN], d_config[DBPW], d_config[DBIP], d_config[DBPT], d_config[USTB], d_config[STTB]]

def _update_config_details(dbun, dbpw, dbip, dbpt, utb, stb) -> int:
    file_handle, d_config = _load_config_file()
    d_config[DBUN] = dbun
    d_config[DBPW] = dbpw 
    d_config[DBIP] = dbip
    d_config[DBPT] = dbpt
    d_config[USTB] = utb
    d_config[STTB] = stb
    try:
        _save_config_file(d_config, file_handle, True)
        return 0
    except:
        return 19

if __name__ == '__main__':
    print(_init_())
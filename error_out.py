
STD_ERR_LST = {
    0 : "OKAY",
    1 : "DENIED",
    2 : "Email is taken",
    3 : "Roll Number already exists",
    4 : "Make sure the face is properly visible",
    5 : "Email already taken :(",
    6 : "Error occured while creating account!",
    7 : "Account does not exist",
    8 : "Wrong Password :/",
    9 : "Try again. contact admin if problem persists",
    10 : "Failed to save the image. Try again!",
    11 : "Error occurred while adding the subject!",
    12 : "Oops! Forgot click the selfie? :p",
    13 : "Error occured while dropping the subject",
    14 : "Specified subject does not exist",
    15 : "Error occured while loading your info :(",
    16 : "Fill all the details",
    17 : "Error while storing attendance!",
    18 : "Initialization Error",
    19 : "Error while saving config file",
    100 : "Account with given mail already exists!", #experimental
}

def ErrorOut(er_num):
    global STD_ERR_LST
    return str(STD_ERR_LST[int(er_num)])


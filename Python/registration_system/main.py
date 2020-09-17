#!usr/bin/env python
from salting import *
from cipher import *
from PyQt5 import uic, QtWidgets
from _datetime import datetime
from datetime import date
import numpy as np
import json, codecs
from PIL import Image
import PIL.ImageOps
from timeit import default_timer as timer
import hashlib
import shutil
import os

"""
TODO:
SOMEWHAT DONE   encorporate the encryptor and credential organiser[]
DONE    fix newlines while updating text
DONE    make registration work
make deciphering images work by pasting path to json file
add dates to enries
"""

app = QtWidgets.QApplication([])
call = uic.loadUi("main_design.ui")
userFiles = os.getcwd() + "/userFiles/"

make_database()


DEBUG = True
# IMAGE = "/home/gotevagyok/Desktop/asd.jpg" # call.addTextBox.toPlainText()
FILES_TO_DELETE = []


def add_timestamp(username):
    personalDir = userFiles + username + "/"
    today = date.today()
    now = datetime.now()
    datum = today.strftime("%B %d %Y")
    timee = now.strftime("%H %M %S")
    with open(personalDir + "dateFile.txt", "r") as PD:
        lastDate = PD.readline()[-1]
        lastDate = "".join(lastDate)
    if datum in lastDate:
        pass

    entry = call.addTextBox.toPlainText() + "\n"
    timestampedEntry = datum + "\n" + timee + ": " + entry


def add_date():
    today = date.today()
    now = datetime.now()
    datum = today.strftime("%B %d %Y")
    hrs = now.strftime("%H")  #:%M:%S")
    mins = now.strftime("%M")
    call.dateLabel.setText(datum)
    call.hrsLabel.setText(hrs)
    call.minsLabel.setText(mins)


def make_user_file(username):
    os.mkdir(userFiles + "/" + username)
    personalDir = userFiles + username + "/"
    with open(personalDir + "dateFile.txt", "a+"):
        pass
    with open(username + "_file.json", "a+") as f:
        f.write("[]")
        shutil.move(username + "_file.json", userFiles + "/" + username)
        pass


def get_data(username):
    entry = call.addTextBox.toPlainText() + "\n"
    if call.timestampCheckBox.isChecked():
        add_timestamp(username)
    else:
        encrypting(userFiles + usrName + "/" + usrName + "_file.json", entry)


def dump_data():
    cleanData = decrypting(userFiles + usrName + "/" + usrName + "_file.json")
    call.storedTextBox.setPlainText(cleanData)
    add_date()


try:
    os.mkdir("userFiles")
except FileExistsError:
    pass


def register():  # function to register user
    usrName = call.regUsrNameTextBox.text()
    if in_database("database.json", usrName):  # checking wether username is taken
        print("Username already taken.")
    else:
        password = call.regPasswTextBox.text()
        password_check = call.regPasswTextBoxCheck.text()
        if password == password_check:
            pw, salt = encrypt(password)  # hashing and salting the password
            update_database("database.json", usrName, pw, salt)  # adding user to the database
            make_user_file(usrName)
            print("Registration succesful!")
        else:
            print("Inconsistent passwords.")


def login():
    global usrName
    usrName = call.usrNameTextBox.text()
    if in_database("database.json", usrName):
        password = call.passwTextBox.text()
        try:
            login_success = decrypt("database.json", usrName, password)
        except KeyError:
            login_success = False
        if login_success:
            print("Login succesful.")
            add_date()
            call.usernameLabel.setText(usrName)
            call.addButton.clicked.connect(get_data)
            call.refreshButton.clicked.connect(dump_data)
        else:
            print("Incorrect password.")
    else:
        print("User not found.")



def debug(stuff):
    if DEBUG:
        print(stuff)

def getImageName(imageLocation):
    im = Image.open(imageLocation)
    imageName = im.filename
    return imageName

def cypherImage():
    global IMAGE
    IMAGE = call.addTextBox.toPlainText()
    global PICNAME
    PICNAME = getImageName(IMAGE)
    hashAndSave()

def deCypherImage():
    global IMAGE
    IMAGE = call.addTextBox.toPlainText()
    global PICNAME
    PICNAME = getImageName(IMAGE)
    justShow(PICNAME)

# PICNAME = getImageName(IMAGE)


def getRGBvalues():
    debug("getting rgb values started")
    """
    getting image as a numpy array of pixel values and returning that array
        Returns:
            nparray of pixels' rgb values
    """
    im = Image.open(PICNAME)
    pixArray = np.asarray(im)
    return pixArray


def saveRGBvalues(pixArray):
    debug("saving rgb values started")
    """
    converting the numpy array of pixels to a storeable format
    to save it in a JSON file.

        Args:
            -pixArray - nparray of rgb values
    """
    global PART1
    PART1 = PICNAME + "_part1.json"
    FILES_TO_DELETE.append(PART1)
    with open(PART1, "a+"):
        data = pixArray.tolist()
        json.dump(data, codecs.open(PART1, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)


def makeImage(JSONfilename):
    debug("making image started")
    """
    Opens JSONfilename and returns the literal picture

        Args:
            Json file containing an nparray of pixel values
        Returns:
            the picture in memory. can show and save it
    """
    obj_text = codecs.open(JSONfilename, 'r', encoding='utf-8').read()
    obj_text = obj_text.replace('"', "")
    b_new = json.loads(obj_text)
    img = np.array(b_new)
    pic = Image.fromarray((img * 255).astype(np.uint8))
    pic = PIL.ImageOps.invert(pic)
    return pic


def hashImage():
    debug("hashing image started")
    """
    Goes through JSONfilename and hashes each character in that file

        Returns:
            Long ass string containing the hash of each character(not divided)
    """
    JSONfilename = PART1
    with open(JSONfilename, "r") as f:
        imgArr = f.read()
    imgArr = str(imgArr)
    with open("cypherDict.json", "r") as f:
        cheatSheet = json.loads(f.read())
    n = 0
    questionableString = ""
    while n < len(imgArr):
        encoded = imgArr[n]#.encode('utf-8')
        # hashed = hashlib.sha256(encoded).hexdigest()
        hashed = cheatSheet[encoded]
        questionableString += hashed
        n += 1
    return questionableString


def saveHash(hashedString):
    debug("saving hash started")
    global HASHED_IMG
    HASHED_IMG = PICNAME + "_ciphered.json"
    with open(HASHED_IMG, "a+") as f:
        f.write(hashedString)


def splitImage(JSONfilename):
    debug("splitting hash started")
    """
    splits the hashed string into chunkSize sized parts to "decipher"

        Args:
            Json file containing the hash of a stringified nparray(letter by letter)
        Returns:
            A list containing each character's hash as an element
    """
    with open(JSONfilename, "r") as f:
        data = f.read()
    chunks = len(data)
    chunkSize = 8
    listOfHash = ([data[i:i+chunkSize] for i in range(0, chunks, chunkSize)])
    return listOfHash


def decipherImage(JSONfilename):
    debug("deciphering hash started")
    """
    compares the divided hashes of the nparray to the dict.json and replaces
    the hash with the corresponding character

        Args:
            Json file containing the hash of a stringified nparray(letter by letter)
        Returns:
            An nparray of the deciphered rgb values
    """
    imgFile = splitImage(JSONfilename)
    i = 0
    decipheredRGB = ""
    with open("decypherDict.json", "r") as f:
        cheatSheet = f.read()
        cheatSheet = json.loads(cheatSheet)
    while i < len(imgFile):
        char = imgFile[i]
        decipheredRGB += cheatSheet[char]
        i += 1
    decipheredRGB = np.asarray(decipheredRGB)
    return decipheredRGB


def save(pixArray):
    global Fname
    Fname = PICNAME + "_part2.json"
    FILES_TO_DELETE.append(Fname)
    with open(Fname, "a+"):
        data = pixArray.tolist()
        json.dump(data, codecs.open(Fname, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)


def cleanUp(filenamesList):
    """
    Removes the unneccessary files left after the process is done

        Args:
            a list containing the filenames that are desired to be removed
    """
    n = 0
    while n < len(filenamesList):
        try:
            os.remove(filenamesList[n])
            debug("File removed: " + filenamesList[n])
            n += 1
        except Exception:
            pass


def hashAndSave():
    """
    hashes and saves the image. cleans up the unneccessary files
    """
    timerStart = timer()
    saveRGBvalues(getRGBvalues())
    saveHash(hashImage())
    save(decipherImage(HASHED_IMG))
    cleanUp(FILES_TO_DELETE)
    timerEnd = timer()
    runTime = timerEnd - timerStart
    debug("Runtime: " + str(runTime)[:6])

def justShow(PICNAME):
    """
    loads the hashed json in and shows it. cleans up the unneccessary files
    Fname needs to be selected by user not hardcoded !
    """
    timerStart = timer()
    # Fname = "test.jpg_ciphered.json"
    HASHED_IMG = PICNAME + "_ciphered.json"
    FILES_TO_DELETE = [PICNAME + "_part2.json"]
    save(decipherImage(HASHED_IMG))
    makeImage(PICNAME + "_part2.json").show()
    cleanUp(FILES_TO_DELETE)
    timerEnd = timer()
    runTime = timerEnd - timerStart
    debug("Runtime: " + str(runTime)[:6])


call.loginButton.clicked.connect(login)
call.registerButton.clicked.connect(register)
call.addImageButton.clicked.connect(cypherImage)
call.showImageButton.clicked.connect(deCypherImage)

call.show()
app.exec_()

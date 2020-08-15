#!usr/bin/env python
from salting import *
from cipher import *
from PyQt5 import uic, QtWidgets
from _datetime import datetime
from datetime import date
import shutil
import os

"""
TODO:
SOMEWHAT DONE   encorporate the encryptor and credential organiser[]
DONE    fix newlines while updating text
DONE    make registration work
add dates to enries
"""

app = QtWidgets.QApplication([])
call = uic.loadUi("main_design.ui")
userFiles = os.getcwd() + "/userFiles/"

make_database()


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


call.loginButton.clicked.connect(login)
call.registerButton.clicked.connect(register)

call.show()
app.exec_()

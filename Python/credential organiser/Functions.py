from PyQt5 import QtWidgets, uic
from _datetime import datetime
from datetime import date
"""
https://stackoverflow.com/questions/9841820/add-text-to-qplaintextedit-in-pyqt-the-result-is-a-status-log
"""


app = QtWidgets.QApplication([])
call = uic.loadUi("mainDesign.ui")


def saveInfo():
    link = call.urlTextBox.text()
    username = call.usernameTextBox.text()
    password = call.passwordTextBox.text()
    notes = call.notesTextBox.toPlainText()

    today = date.today()
    now = datetime.now()
    datum = today.strftime("%B %d %Y")
    hrs = now.strftime("%H:%M:%S")

    with open("totallyNotPasswords.txt", "a+") as f:
        f.write("added: " + datum + " " + hrs + "\n")
        f.write("website: " + link + "\n")
        f.write("   username: " + username + "\n")
        f.write("   password: " + password + "\n")
        f.write("   notes: " + notes + "\n\n")
        print("added succesfully")

call.saveButton.clicked.connect(saveInfo)

call.show()
app.exec_()

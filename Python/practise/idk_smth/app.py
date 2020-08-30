from userClass import user
import json
from PyQt5 import uic, QtWidgets



app = QtWidgets.QApplication([])
dialog = QMessageBox()

def showDialog():
    QDialog.setWindowTitle("Login")




call = uic.loadUi("mainUI.ui")



with open("db.json", "r") as db:
    data = db.read()
    users = json.loads(data)

username = ""
password = ""
password_check = ""


currentUser = user(username, password, password_check, users)

def openMain():
    call.show()
    app.exec_()


QDialog.loginButton.clicked.connect()

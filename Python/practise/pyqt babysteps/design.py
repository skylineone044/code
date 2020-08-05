# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(600, 750)
        self.encFromFileButton = QtWidgets.QPushButton(mainWindow)
        self.encFromFileButton.setGeometry(QtCore.QRect(220, 640, 151, 38))
        self.encFromFileButton.setObjectName("encFromFileButton")
        self.decrFromFileButton = QtWidgets.QPushButton(mainWindow)
        self.decrFromFileButton.setGeometry(QtCore.QRect(220, 690, 151, 38))
        self.decrFromFileButton.setObjectName("decrFromFileButton")
        self.encTextBox = QtWidgets.QLineEdit(mainWindow)
        self.encTextBox.setGeometry(QtCore.QRect(40, 30, 511, 171))
        self.encTextBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.encTextBox.setObjectName("encTextBox")
        self.decTextBox = QtWidgets.QLineEdit(mainWindow)
        self.decTextBox.setGeometry(QtCore.QRect(40, 270, 511, 241))
        self.decTextBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.decTextBox.setObjectName("decTextBox")
        self.encryptButton = QtWidgets.QPushButton(mainWindow)
        self.encryptButton.setGeometry(QtCore.QRect(220, 210, 151, 38))
        self.encryptButton.setObjectName("encryptButton")
        self.decryptButton = QtWidgets.QPushButton(mainWindow)
        self.decryptButton.setGeometry(QtCore.QRect(220, 540, 151, 38))
        self.decryptButton.setObjectName("decryptButton")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Dialog"))
        self.encFromFileButton.setText(_translate("mainWindow", "Encrypt from file"))
        self.decrFromFileButton.setText(_translate("mainWindow", "Decrypt from file"))
        self.encTextBox.setText(_translate("mainWindow", ""))
        self.decTextBox.setText(_translate("mainWindow", ""))
        self.encryptButton.setText(_translate("mainWindow", "Encrypt"))
        self.decryptButton.setText(_translate("mainWindow", "Decrypt"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QDialog()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

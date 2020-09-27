from QoL import PATH, DB, USERFILES_PATH, debug
from timeit import default_timer as timer
from security import Sec
import shutil
import json
import os


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.filePath = USERFILES_PATH + self.username + "\\"

    def inDB(self, username):
        """
        Checks wether username is already taken
        """
        with open(DB, "r") as database:
            dbContents = json.loads(database.read())
        if self.username in dbContents:
            return True
        else:
            return False

    def makeUserFile(self, username):
        os.mkdir(USERFILES_PATH + self.username)
        with open(self.filePath + self.username + ".json", "a+") as userFile:
            bracket = json.dumps([])
            userFile.write(bracket)

    def register(self, username, password):
        """
        Registers the user, stored in DB,
        checks if username is already taken
        """
        if not self.inDB(self.username):
            self.makeUserFile(self.username)
            with open(DB, "r") as database:
                dbContents = json.loads(database.read())
            self.password = Sec(self.username, self.password)
            self.password, self.salt = self.password.encrypt(self.password)
            dbContents.update({self.username: [self.password, self.salt]})
            with open(DB, "w") as database:
                updatedDB = json.dumps(dbContents, sort_keys=True, indent=4)
                database.write(updatedDB)
            debug("REG | username : " + self.username +
                  ", password: " + self.password[:8])
        else:
            debug("REG | user " + self.username + " already in database")

    def loggedIn(self, username, password):
        if self.inDB(self.username):
            with open(DB, "r") as database:
                dbContents = json.loads(database.read())
            pw = Sec(self.username, self.password)
            self.password = pw.decrypt(self.username, self.password)
            if self.password == dbContents[self.username][0]:
                debug("LOGIN | " + self.username + " SUCCESS")
                return True
            else:
                debug("LOGIN | " + self.username + " FAILED")
                return False
        else:
            debug("LOGIN | " + self.username + " NOT FOUND")
            return False

    def deleteUser(self, username):
        with open(DB, "r") as database:
            with open(DB, "r") as database:
                dbContents = json.loads(database.read())
                del dbContents[self.username]
            with open(DB, "w") as database:
                updatedDB = json.dumps(dbContents, sort_keys=True, indent=4)
                database.write(updatedDB)
            shutil.rmtree(USERFILES_PATH + self.username)
            debug("DEL | username: " + self.username)

    def addText(self, username, text):
        textToAdd = Sec(self.username, self.password)
        hashedText = textToAdd.cipher(self.username, text)
        with open(self.filePath + self.username + ".json", "w") as userFile:
            userFile.write(json.dumps(hashedText, indent=4))
        debug("ADDTXT | SUCCESSFUL")

    def showText(self, username):
        stuff = Sec(self.username, self.password)
        cleanText = stuff.decipher(
            self.username, self.filePath + self.username + ".json")
        print(cleanText)

    def addTimeStamp(self, username):
        pass

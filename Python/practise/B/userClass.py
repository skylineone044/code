from timeit import default_timer as timer
from QoL import PATH, DB_PATH, USERFILES_PATH, debug
import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def inDB(self, username):
        """
        Checks wether username is already taken
        """
        with open(DB_PATH, "r") as database:
            dbContents = json.loads(database.read())
        if self.username in dbContents:
            return True
        else:
            return False


    def register(self, username, password):
        """
        Registers the user, stored in DB_PATH,
        checks if username is already taken
        """
        if not self.inDB(self.username):
            with open(DB_PATH, "r") as database:
                dbContents = json.loads(database.read())
            dbContents.update({self.username: self.password})
            with open(DB_PATH, "w") as database:
                updatedDB = json.dumps(dbContents, sort_keys=True, indent=4)
                database.write(updatedDB)
            debug("REG | username : " + self.username + ", password: " + self.password)
        else:
            debug("REG | user " + self.username + " already in database")


    def login(self, username, password):
        if self.inDB(self.username):
            with open(DB_PATH, "r") as database:
                dbContents = json.loads(database.read())
            if self.password == dbContents[self.username]:
                debug("LOGIN | " + self.username + " SUCCESS")
                return True
            else:
                debug("LOGIN | " + self.username + " FAILED")
                return False
        else:
            debug("LOGIN | " + self.username + " NOT FOUND")
            return False



            
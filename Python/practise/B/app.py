from QoL import PATH, DB, USERFILES_PATH, debug
from _datetime import datetime
from datetime import date
from security import Sec
from userClass import User
from utils import setup


"""
TODO 
DONE    create DB in DB automatically
DONE    create files for users in USERFILES_PATH
DONE    salt passwords
DONE    salt and hash text input
DONE    decipher stored text
    create UI
    maybe add img support

"""
setup()


def testAcc(UN, PW):
    user = User(UN, PW)
    # user.register(user.username, user.password)
    # user.loggedIn(user.username, user.password)
    # user.addText(user.username, "yeah boiiiiii")
    user.deleteUser(user.username)
    # user.showText(UN)


testAcc("asd", "asd")


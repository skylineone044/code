from QoL import PATH, DB, USERFILES_PATH, debug
from security import Sec
from userClass import User
from utils import setup

"""
TODO 
DONE    create DB in DB automatically
DONE    create files for users in USERFILES_PATH
DONE    salt passwords
DONE    salt and hash text input
    decipher stored text
    create UI
    maybe add img support

"""
setup()

def testAcc(UN, PW):
    user = User(UN, PW)
    # user.register(user.username, user.password)
    # user.loggedIn(user.username, user.password)
    # user.addText(user.username, "asdasd uagfuskldcví75sdfsö89vöí8")
    user.deleteUser(user.username)
    # user.showText(UN)


testAcc("Gote", "asd")


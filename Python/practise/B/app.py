from QoL import PATH, DB, USERFILES_PATH, debug
from security import Sec
from userClass import User
from utils import setup

"""
TODO 
    create DB in DB automatically
    create files for users in USERFILES_PATH
    salt passwords

"""
setup()
# me = User("Gote", "asd")
me = User("Beno", "asd")
# me.register(me.username, me.password)
# me.login(me.username, me.password)
me.deleteUser(me.username)

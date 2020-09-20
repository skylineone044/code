from userClass import User
from QoL import PATH, DB_PATH, USERFILES_PATH, debug
from utils import setup

"""
TODO 
    create DB in DB_PATH automatically
    create files for users in USERFILES_PATH
    salt passwords

"""
setup()

# me = User("Beno", "asd")
# me.register(me.username, me.password)
# me.login(me.username, me.password)
import os

DEBUG = True
PATH = os.getcwd()
DB = PATH + "\\database\\database.json"
USERFILES_PATH = PATH + "\\userFiles\\"
SALT_LENGTH = 10
CHAR_FILE = PATH + "\\database\\charList.json"



def debug(msg):
    if DEBUG:
        print(msg)

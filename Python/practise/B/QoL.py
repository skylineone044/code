import os

DEBUG = True
PATH = os.getcwd()
DB_PATH = PATH + "\\database\\database.json"
USERFILES_PATH = PATH + "\\userFiles"


def debug(msg):
    if DEBUG:
        print(msg)
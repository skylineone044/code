from QoL import PATH, DB, debug
import os
import json


def setup():
    """
    sets up necessary directories 
    """
    try:
        os.mkdir(PATH + "\\database")
        os.mkdir(PATH + "\\userFiles")
        debug("SETUP | clreated DB, USER_FILES dirs")
    except FileExistsError:
        pass
    with open(DB, "a+"):
        pass
    with open(PATH + "\\database\\charList.json", "a+") as charList:
        pass
    if os.stat(PATH + "\\database\\charList.json").st_size == 0:
        with open(PATH + "\\database\\charList.json", "w") as charList:
            json.dumps(charList.write("[]"))
    if os.stat(DB).st_size == 0:
        with open(DB, "w") as db:
            json.dumps(db.write("{}"))

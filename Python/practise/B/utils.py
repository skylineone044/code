from QoL import PATH, DB, debug
import os
import json


def setup():
    try:
        os.mkdir(PATH + "\\database")
        os.mkdir(PATH + "\\userFiles")
        debug("SETUP | clreated DB, USER_FILES dirs")
    except FileExistsError:
        pass
    with open(DB, "a+"):
        pass
    if os.stat(DB).st_size == 0:
        with open(DB, "w") as db:
            json.dumps(db.write("{}"))

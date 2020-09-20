from QoL import PATH, DB_PATH, debug
import os
import json

def setup():
    try: 
        os.mkdir(PATH + "\\database")
        os.mkdir(PATH + "\\userFiles")
    except FileExistsError:
        pass
    
    if os.stat(DB_PATH).st_size == 0:
        with open(DB_PATH, "w") as db:
            json.dumps(db.write("{}"))
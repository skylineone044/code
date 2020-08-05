import hashlib
import random
import json
import os

saltList = ["q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "a",
            "s", "d", "f", "g", "h", "j", "k", "l", "y", "x", "c",
            "v", "b", "n", "m", "0", "1", "2", "3", "4", "5", "6",
            "7", "8", "9"
            ]


# start of functions-------------------------------------------------------------

def make_database():
    with open("database.json", "a+") as dbFile:
        if os.stat("database.json").st_size == 0:
            dbFile.write("{}")
        else:
            pass


def update_database(dbLocation, username, hashedPassword, salt):
    with open(dbLocation, "r") as dbFile:
        raw_data = dbFile.read()
        array = json.loads(raw_data)
    creds = hashedPassword, salt
    array.update({username: creds})
    with open(dbLocation, "w") as dbFile:
        Jdata = json.dumps(array, sort_keys=True, indent=4)
        dbFile.write(Jdata)


def in_database(dbLocation, username):
    with open(dbLocation, "r") as dbFile:
        raw_data = dbFile.read()
        if username in raw_data:
            return True
        else:
            return False


def encrypt(password):
    n = 0
    salt = []
    while n < 10:
        char = random.choice(saltList)
        number = random.randint(0, 1)
        if number == 0:
            char = char.lower()
        else:
            char = char.upper()
        salt.append(char)
        n += 1
    salt = "".join(salt)
    pw = password + salt
    pw = pw.encode('utf-8')
    pw = hashlib.sha256(pw).hexdigest()
    return pw, salt


def decrypt(dbLocation, username, password):
    with open(dbLocation, "r", encoding='utf-8') as database:
        raw_data = database.read()
        users = json.loads(raw_data)
    load_salt = users[username][1]
    raw_password = password + load_salt
    raw_password = raw_password.encode('utf-8')
    processed_password = hashlib.sha256(raw_password).hexdigest()
    saved_password = users[username][0]
    if processed_password == saved_password:
        return True
    else:
        return False

# end of functions---------------------------------------------------------------

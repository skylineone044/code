from QoL import SALT_LENGTH, DB, debug
import hashlib
import random
import json
import os


saltList = [
    "q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "a",
    "s", "d", "f", "g", "h", "j", "k", "l", "y", "x", "c",
    "v", "b", "n", "m", "0", "1", "2", "3", "4", "5", "6",
    "7", "8", "9"
]


class Sec:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def encrypt(self, password):
        n = 0
        salt = ""
        while n < SALT_LENGTH:
            char = random.choice(saltList)
            number = random.randint(0, 1)
            if number == 0:
                char = char.lower()
            else:
                char = char.lower()
            salt += char
            n += 1
        pw = self.password + salt
        pw = pw.encode('utf-8')
        pw = hashlib.sha256(pw).hexdigest()
        return pw, salt

    def decrypt(self, username, password):
        with open(DB, "r") as database:
            dbContents = json.loads(database.read())
        salt = dbContents[self.username][1]
        pw = self.password + salt
        pw = pw.encode('utf-8')
        pw = hashlib.sha256(pw).hexdigest()
        return pw



        
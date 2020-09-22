from QoL import USERFILES_PATH, SALT_LENGTH, DB, debug
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
        """
        generates a random salt, mixes it with password and hashes it

        Args:
            password to mix with salt

        Returns:
            pw - (password mixed with salt) hashed
            salt - the random string of characters 
        """
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
        """
        hashes password + salt to get the user's pw

        Args:
            username to locate user's salt
            password to mix with salt and hash

        Returns:
            hash of password+salt
        """
        with open(DB, "r") as database:
            dbContents = json.loads(database.read())
        salt = dbContents[self.username][1]
        pw = self.password + salt
        pw = pw.encode('utf-8')
        pw = hashlib.sha256(pw).hexdigest()
        return pw

    def cipher(self, username, text):
        """
        hashes text+user's salt together for added security

        Args:
            username to locate user's file and salt
            text to have something to cipher

        Returns:
            List of hashed characters, each char as an element
        """
        n = 0
        self.text = text + "\n"
        with open(DB, "r") as database:
            dbContents = json.loads(database.read())
        self.salt = dbContents[self.username][1]
        with open(USERFILES_PATH + self.username + ".json") as userFile:
            userFileData = json.loads(userFile.read())
        while n < len(self.text):
            char = (self.text[n] + self.salt).encode('utf-8')
            char = hashlib.sha256(char).hexdigest()
            userFileData.append(char)
            n += 1
        debug("CIP | SUCCESFUL")
        return userFileData

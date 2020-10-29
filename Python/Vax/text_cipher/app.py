import hashlib
import json
import os


FILE_NAME = "test.txt"


def makeFiles():
    with open("charList.json", "a+"):
        pass
    with open("cipheredText.json", "a+"):
        pass
    if os.stat("charList.json").st_size == 0:
        with open("charList.json", "w") as charFile:
            json.dumps(charFile.write("[]"))
    if os.stat("cipheredText.json").st_size == 0:
        with open("cipheredText.json", "w") as charFile:
            json.dumps(charFile.write("[]"))


def saveCharList(newList):
    with open("charList.json", "w") as charFile:
        charFile.write(json.dumps(newList, indent=4))


def saveCipText(text):
    with open("cipheredText.json", "r") as f:
        cipTextList = json.loads(f.read())
    cipTextList = cipTextList + text
    with open("cipheredText.json", "w") as f:
        f.write(json.dumps(cipTextList, indent=4))


def extractText(fileLocation):
    with open(fileLocation, "r") as f:
        plainText = f.read()
    i = 0
    characters = []
    while i < len(plainText):
        characters.append(plainText[i])
        i += 1
    return characters


def updateCharList():
    with open("charList.json", "r") as charFile:
        charList = json.loads(charFile.read())
    userText = extractText(FILE_NAME)
    n = 0
    while n < len(userText):
        if userText[n] not in charList:
            charList.append(userText[n])
        n += 1
    saveCharList(sorted(charList))


def cipherPlainText():
    updateCharList()
    userText = extractText(FILE_NAME)
    k = 0
    cipheredList = []
    while k < len(userText):
        char = userText[k].encode("utf-8")
        char = hashlib.sha256(char).hexdigest()
        cipheredList.append(char)
        k += 1
    saveCipText(cipheredList)


def cheatSheet():
    with open("charList.json", "r") as charFile:
        chars = json.loads(charFile.read())
    i = 0
    cheatSheet = {}
    while i < len(chars):
        char = chars[i]
        charC = char.encode("utf-8")
        charC = hashlib.sha256(charC).hexdigest()
        cheatSheet.update({charC: char})
        i += 1
    return cheatSheet


def cleanUp():
    with open(FILE_NAME, "w") as f:
        f.write("")


def decipher():
    with open("cipheredText.json", "r") as f:
        cipText = json.loads(f.read())
    clearText = ""
    i = 0
    decode = cheatSheet()
    while i < len(cipText):
        char = cipText[i]
        clearText += decode[char]
        i += 1
    return clearText


makeFiles()
cipherPlainText()
print(decipher())
cleanUp()

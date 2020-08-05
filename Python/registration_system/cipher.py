import hashlib
import json
import os


# what does this do
def encrypting(user_file, data):
    with open(user_file, "r") as f:
        rawData = f.read()
        userData = json.loads(rawData)
    toEncr = data
    toEncr = toEncr.replace("\n", "¤")
    if len(toEncr) == 0:
        successInWriting = False
    else:
        successInWriting = True
    i = 0
    length = len(toEncr)
    while i < length:
        # iterating through every character and hashing it
        toEncr1 = toEncr[i]
        data = toEncr1.encode('utf-8')
        doneEncr = hashlib.sha256(data).hexdigest()
        userData.append(doneEncr)
        i += 1

    with open(user_file, "w", encoding='utf-8') as JFile:
        # saving hashed data
        data = json.dumps(userData, sort_keys=True, indent=4)
        JFile.write(data)
    if successInWriting:
        print("Encryption successful!")
    else:
        print("No data to encrypt!")


def decrypting(user_file):
    with open(user_file, "r") as JFile:
        try:
            # trying to read data to decrypt
            data = JFile.read()
            toDecr = json.loads(data)
            length = len(toDecr)
        except json.decoder.JSONDecodeError:
            # this error is thrown when nothing is in the file
            length = 0
            print("No data to decrypt!")
    if length == 0:
        succesInReading = False
    else:
        succesInReading = True

    with open("dict.json", "r") as keys:
        # loading the hashes of the characters into memory
        data = keys.read().encode('utf-8')
        fullDict = json.loads(data)

    i = 0
    fulltext = ""
    while i < length:
        currLine = toDecr[i]
        if currLine in fullDict:
            # if the current character is in the dict.json
            if fullDict[currLine] == "¤":
                fulltext += "\n"
            else:
                fulltext += (fullDict[currLine])

        else:
            # if the caharacter is not in dict.json we write [x]
            fulltext += "[x]"
        i += 1
    if succesInReading:
        print("Decription succesful!")
    else:
        print("No data to decrypt!")
    return fulltext

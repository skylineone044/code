from PIL import Image
import PIL.ImageOps
import json, codecs
import numpy as np
import hashlib
import os

# TODO
#   Need to store image's w and h in image's json file some way
#   Maybe even the metadata(last modified, size and interesting shit)
#       -save the JSON of img and a txt of metadata to img's folder
# DONE  split hashed chars at each line to make de-cyphering it easier
# XD  also add salt to each char <- Fuck that shit all my homies hate salt
#   strip deciphered ndarrray of "s (indexes 0 and -1)
#   a bug occours when reading and/or saving rgb data as a string. need to
#   convert it to nparray




DEBUG = True

def debug(stuff):
    if DEBUG:
        print(stuff)


def getRGBvalues(picture):
    debug("getting rgb values started")
    """
    getting image as a numpy array of pixel values and returning that array
        Args:
            literal image file as a string eg.: C\\ImagesOfCats\\cat.png
        Returns:
            nparray of pixels' rgb values
    """
    im = Image.open(picture)
    pixArray = np.asarray(im)
    return pixArray


def saveRGBvalues(JSONfilename, pixArray):
    debug("saving rgb values started")
    """
    converting the numpy array of pixels to a storeable format
    to save it in a JSON file.
        Args:
            -JSONfilename - name of the json file that will be created
            -pixArray - nparray of rgb values

    """
    with open(JSONfilename, "a+") as f:
        data = pixArray.tolist()
        json.dump(data, codecs.open(JSONfilename, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)


def makeImage(JSONfilename):
    debug("making image started")
    """
    Opens JSONfilename and returns the literal picture

        Args:
            Json file containing an nparray of pixel values
        Returns:
            the picture in memory. can show and save it
    """
    obj_text = codecs.open(JSONfilename, 'r', encoding='utf-8').read()
    obj_text = obj_text.replace('"', "")
    b_new = json.loads(obj_text)
    img = np.array(b_new)
    pic = Image.fromarray((img * 255).astype(np.uint8))
    pic = PIL.ImageOps.invert(pic)
    return pic


def hashImage(JSONfilename):
    debug("hashing image started")
    with open(JSONfilename, "r") as f:
        imgArr = f.read()
    imgArr = str(imgArr)
    n = 0
    questionableString = ""
    while n < len(imgArr):
        encoded = imgArr[n].encode('utf-8')
        hashed = hashlib.sha256(encoded).hexdigest()
        questionableString += hashed
        n += 1
    return questionableString


def saveHash(JSONfilename, hashedString):
    debug("saving hash started")
    with open(JSONfilename, "a+") as f:
        f.write(hashedString)


def splitImage(JSONfilename):
    debug("splitting hash started")
    with open(JSONfilename, "r") as f:
        data = f.read()
    chunks = len(data)
    chunkSize = 64
    listOfHash = ([data[i:i+chunkSize] for i in range(0, chunks, chunkSize)])
    return listOfHash


def decipherImage(JSONfilename):
    imgFile = splitImage(JSONfilename)
    i = 0
    decipheredRGB = ""
    with open("dict.json", "r") as f:
        cheatSheet = f.read()
        cheatSheet = json.loads(cheatSheet)
    debug("deciphering hash started")
    while i < len(imgFile):
        char = imgFile[i]
        decipheredRGB += cheatSheet[char]
        i += 1
    decipheredRGB = np.asarray(decipheredRGB)
    return decipheredRGB


def save(pixArray):
    with open("JSONfilename.json", "a+") as f:
        data = pixArray.tolist()
        json.dump(data, codecs.open("JSONfilename.json", 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)


def removeFiles(filenamesList):
    n = 0
    while n < len(filenamesList):
        os.remove(filenamesList[n])
        debug("File removed: " + filenamesList[n])
        n += 1

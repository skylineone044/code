from PIL import Image
import PIL.ImageOps
import json, codecs
import numpy as np
import hashlib

# TODO
#   Need to store image's w and h in image's json file some way
#   Maybe even the metadata(last modified, size and interesting shit)
#       -save the JSON of img and a txt of metadata to img's folder
# DONE  split hashed chars at each line to make de-cyphering it easier
# XD  also add salt to each char <- Fuck that shit all my homies hate salt
#   strip deciphered ndarrray of "s (indexes 0 and -1)
#   a bug occours when reading and/or saving rgb data as a string. need to
#   convert it to nparray




DEBUG = False

def debug(stuff):
    if DEBUG:
        print(stuff)


def getRGBvalues(picture):
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
    """
    Opens JSONfilename and returns the literal picture

        Args:
            Json file containing an nparray of pixel values
        Returns:
            the picture in memory. can show and save it
    """
    obj_text = codecs.open(JSONfilename, 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    img = np.array(b_new)
    pic = Image.fromarray((img * 255).astype(np.uint8))
    pic = PIL.ImageOps.invert(pic)
    return pic


def hashImage(pixArray):
    # with open(JSONfilename, "r") as f:
    #     imgArr = f.read()
    imgArr = pixArray.tostring()
    imgArr = str(imgArr)
    debug(imgArr)
    n = 0
    questionableString = ""
    while n < len(imgArr):
        encoded = imgArr[n].encode('utf-8')
        hashed = hashlib.sha256(encoded).hexdigest()
        questionableString += hashed
        n += 1
    return questionableString



def splitImage(JSONfilename):
    with open(JSONfilename, "r") as f:
        data = f.read()
    chunks = len(data)
    chunkSize = 64
    listOfHash = ([data[i:i+chunkSize] for i in range(0, chunks, chunkSize)])
    debug(listOfHash)
    return listOfHash


def decipherImage(JSONfilename):
    imgFile = splitImage(JSONfilename)
    i = 0
    decipheredRGB = ""
    with open("dict.json", "r") as f:
        cheatSheet = f.read()
        cheatSheet = json.loads(cheatSheet)
    while i < len(imgFile):
        char = imgFile[i]
        try:
            decipheredRGB += cheatSheet[char]
        except KeyError:
            pass
        i += 1
    debug(decipheredRGB)
    #decipheredRGB.strip('"')             # important, not sure if works
    decipheredRGB = np.asarray(decipheredRGB)
    return decipheredRGB

def save(pixArray):
    with open("JSONfilename.json", "a+") as f:
        data = pixArray.tolist()
        json.dump(data, codecs.open("JSONfilename.json", 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)

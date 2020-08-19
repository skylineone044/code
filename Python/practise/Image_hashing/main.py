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
# figure out how to just save and just show an image




DEBUG = True
IMAGE = "test.jpg"
FILES_TO_DELETE = []


def debug(stuff):
    if DEBUG:
        print(stuff)

def getImageName():
    im = Image.open(IMAGE)
    imageName = im.filename
    return imageName


PICNAME = getImageName()


def getRGBvalues():
    debug("getting rgb values started")
    """
    getting image as a numpy array of pixel values and returning that array
        Returns:
            nparray of pixels' rgb values
    """
    im = Image.open(PICNAME)
    pixArray = np.asarray(im)
    return pixArray


def saveRGBvalues(pixArray):
    debug("saving rgb values started")
    """
    converting the numpy array of pixels to a storeable format
    to save it in a JSON file.

        Args:
            -pixArray - nparray of rgb values
    """
    global PART1
    PART1 = PICNAME + "_part1.json"
    FILES_TO_DELETE.append(PART1)
    with open(PART1, "a+") as f:
        data = pixArray.tolist()
        json.dump(data, codecs.open(PART1, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)


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


def hashImage():
    debug("hashing image started")
    """
    Goes through JSONfilename and hashes each character in that file

        Returns:
            Long ass string containing the hash of each character(not divided)
    """
    JSONfilename = PART1
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


def saveHash(hashedString):
    debug("saving hash started")
    global HASHED_IMG
    HASHED_IMG = PICNAME + "_ciphered.json"
    with open(HASHED_IMG, "a+") as f:
        f.write(hashedString)


def splitImage(JSONfilename):
    debug("splitting hash started")
    """
    splits the hashed string into chunkSize sized parts to "decipher"

        Args:
            Json file containing the hash of a stringified nparray(letter by letter)
        Returns:
            A list containing each character's hash as an element
    """
    with open(JSONfilename, "r") as f:
        data = f.read()
    chunks = len(data)
    chunkSize = 64
    listOfHash = ([data[i:i+chunkSize] for i in range(0, chunks, chunkSize)])
    return listOfHash


def decipherImage(JSONfilename):
    debug("deciphering hash started")
    """
    compares the divided hashes of the nparray to the dict.json and replaces
    the hash with the corresponding character

        Args:
            Json file containing the hash of a stringified nparray(letter by letter)
        Returns:
            An nparray of the deciphered rgb values
    """
    imgFile = splitImage(JSONfilename)
    i = 0
    decipheredRGB = ""
    with open("dict.json", "r") as f:
        cheatSheet = f.read()
        cheatSheet = json.loads(cheatSheet)
    while i < len(imgFile):
        char = imgFile[i]
        decipheredRGB += cheatSheet[char]
        i += 1
    decipheredRGB = np.asarray(decipheredRGB)
    return decipheredRGB


def save(pixArray):
    global Fname
    Fname = PICNAME + "_part2.json"
    FILES_TO_DELETE.append(Fname)
    with open(Fname, "a+") as f:
        data = pixArray.tolist()
        json.dump(data, codecs.open(Fname, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)


def removeFiles(filenamesList):
    """
    Removes the unneccessary files left after the process is done

        Args:
            a list containing the filenames that are desired to be removed
    """
    n = 0
    while n < len(filenamesList):
        os.remove(filenamesList[n])
        debug("File removed: " + filenamesList[n])
        n += 1


def hashAndSave():
    """
    hashes and saves the image. cleans up the unneccessary files
    """
    saveRGBvalues(getRGBvalues())
    saveHash(hashImage())
    save(decipherImage(HASHED_IMG))
    removeFiles(FILES_TO_DELETE)

def justShow():
    """
    loads the hashed json in and shows it. cleans up the unneccessary files
    Fname needs to be selected by user not hardcoded !
    """
    Fname = "test.jpg_ciphered.json"
    HASHED_IMG = PICNAME + "_ciphered.json"
    FILES_TO_DELETE = [PICNAME + "_part2.json"]
    save(decipherImage(HASHED_IMG))
    makeImage(PICNAME + "_part2.json").show()
    removeFiles(FILES_TO_DELETE)


def main():
    # hashAndSave()
    # justShow()

main()

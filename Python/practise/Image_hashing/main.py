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




DEBUG = False

def debug(stuff):
    if DEBUG:
        print(stuff)


def getRGBdata(imageName):
    """
    UNUSED!
    function to open an image (passed in as a str.) and get every pixel's
    RGB value. returns a list with all the values
    """
    im = Image.open(imageName)
    pic = im.load()
    lst = []
    x = 0
    y = 0
    width = im.size[0]
    height = im.size[1]
    print(width)
    print(height)
    while y < height:
        x = 0
        while x < width:
            pix = pic[x, y]
            lst.append(pix)
            x += 1
            debug(x)
        y += 1
        debug(y)
    return lst


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


def makeSalt():
    """
    UNUSED!
    makes a salt to further strenghten the decipheredRGB
        Returns:
            5 character long string of random content(see saltList)
    """
    saltList = [
                "q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "a",
                "s", "d", "f", "g", "h", "j", "k", "l", "y", "x", "c",
                "v", "b", "n", "m", "0", "1", "2", "3", "4", "5", "6",
                "7", "8", "9"
                ]
    n = 0
    salt = ""
    while n < 5:
        num = random.randint(0, 1)
        char = random.choice(saltList)
        if num == 0:
            char = char.upper()
        salt + char
        n += 1
        debug(salt)
    return salt


def hashImage(JSONfilename):
    """
    obj_text = codecs.open(JSONfilename, 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    imgArr = np.array(b_new)
    """
    with open(JSONfilename, "r") as f:
        imgArr = f.read()
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

# data = hashImage("hello.json")
# with open("hashedIMG.json", "a+") as f:
#     f.write(data)


def splitImage(JSONfilename):
    with open(JSONfilename, "r") as f:
        data = f.read()
    chunks = len(data)
    chunkSize = 64
    listOfHash = ([data[i:i+chunkSize] for i in range(0, chunks, chunkSize)])
    debug(listOfHash)
    return listOfHash


#splitImage("hashedIMG.json")

def decipherImage(JSONfilename):
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
    debug(decipheredRGB)
    decipheredRGB.replace('"', "")              # important, not sure if works
    decipheredRGB = np.asarray(decipheredRGB)
    return decipheredRGB


#data = decipherImage("hashedIMG.json")

#with open("asd.json", "a+") as f:


def save(pixArray):
    with open("JSONfilename.json", "a+") as f:
        data = pixArray.tolist()
        json.dump(data, codecs.open("JSONfilename.json", 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)

#save(data)

makeImage("JSONfilename.json").show()

#show(decipherImage("hashedIMG.json"))

# print(type(decipherImage("hashedIMG.json")))


#decipherImage("hashedIMG.json")

#myData = getRGBvalues("test.jpg")
#saveRGBvalues("hello.json", myData)
#makeImage("hello.json").show()

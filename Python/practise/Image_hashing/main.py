from PIL import Image
import PIL.ImageOps
import json, codecs
import numpy as np

# TODO
#   Need to store image's w and h in image's json file some way
#   Maybe even the metadata(last modified, size and interesting shit)

def getRGBdata(imageName):
    """
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
            #print("x: " + str(x))
        y += 1
        #print("y: " + str(y))
    return lst


def getRGBvalues(picture):
    im = Image.open(picture)
    pixArray = np.asarray(im)
    return pixArray


def saveRGBvalues(JSONfilename, pixArray):
    with open(JSONfilename, "a+") as f:
        data = pixArray.tolist()
        json.dump(data, codecs.open(JSONfilename, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)


def makeImage(JSONfilename):
    obj_text = codecs.open(JSONfilename, 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    img = np.array(b_new)
    pic = Image.fromarray((img * 255).astype(np.uint8))
    pic = PIL.ImageOps.invert(pic)
    return pic


#myData = getRGBvalues("test.jpg")
#saveRGBvalues("hello.json", myData)
makeImage("hello.json").show()

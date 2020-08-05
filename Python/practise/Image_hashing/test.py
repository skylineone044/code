from PIL import Image
import PIL.ImageOps
import json, codecs
import numpy as np

"""
im = Image.open('test.jpg')
a = np.asarray(im)

with open("data.json", "a+") as f:
    data = a.tolist()
    json.dump(data, codecs.open("asd.json", 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)


"""

# im = Image.fromarray(a)


def getRGBvalues(picture):
    im = Image.open(picture)
    pixArray = np.asarray(im)
    return pixArray


def saveRGBvalues(JSONfilename, pixArray):
    with open(JSONfilename, "a+") as f:
        data = a.tolist()
        json.dump(data, codecs.open("asd.json", 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)


def makeImage(JSONfilename):
    obj_text = codecs.open(JSONfilename, 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    img = np.array(b_new)
    pic = Image.fromarray((img * 255).astype(np.uint8))
    pic = PIL.ImageOps.invert(pic)
    return pic



makeImage("asd.json").show()

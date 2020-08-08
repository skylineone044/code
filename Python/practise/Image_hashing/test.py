"""

from PIL import Image
import PIL.ImageOps
import json, codecs
import numpy as np


im = Image.open('test.jpg')
a = np.asarray(im)

with open("data.json", "a+") as f:
    data = a.tolist()
    json.dump(data, codecs.open("asd.json", 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)




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
"""



"""
n = 0
k = 0
string = ""
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
while n < 10:
    letter = lista[k]
    string += 64 * letter
    k += 1
    n += 1
"""

# https://stackoverflow.com/questions/9475241/split-string-every-nth-character
chunks = len(string)
chunk_size = 64

print([string[i:i+chunk_size] for i in range(0, chunks, chunk_size)])
# splits text into chunk_size sized parts and returns a list with 64len items

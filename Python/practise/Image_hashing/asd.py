from main import *
from PIL import Image
import PIL.ImageOps
import json, codecs
import numpy as np
import hashlib

# saveRGBvalues("alap.json", getRGBvalues("test.jpg"))

#
# data = hashImage("alap.json")
# with open("hashedIMG.json", "a+") as f:
#     f.write(data)

# save(decipherImage("hashedIMG.json"))
#
makeImage("JSONfilename.json").show()

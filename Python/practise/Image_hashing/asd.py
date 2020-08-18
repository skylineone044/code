from main import *
from PIL import Image
import PIL.ImageOps
import json, codecs
import numpy as np
import hashlib


def main():
    saveRGBvalues("alap.json", getRGBvalues("test.jpg"))
    saveHash("hashedIMG.json", hashImage("alap.json"))
    save(decipherImage("hashedIMG.json"))
    makeImage("JSONfilename.json").show()
    filesToRemove = ["alap.json", "JSONfilename.json"]
    removeFiles(filesToRemove)

main()

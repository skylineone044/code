from main import *
from PIL import Image
import PIL.ImageOps
import json, codecs
import numpy as np
import hashlib


def main():
    saveRGBvalues(getRGBvalues())
    saveHash(hashImage())
    save(decipherImage(HASHED_IMG))
    makeImage("JSONfilename.json").show()
    # filesToRemove = ["alap.json", "JSONfilename.json"]
    removeFiles(FILES_TO_DELETE)

main()

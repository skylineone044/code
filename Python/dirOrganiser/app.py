import shutil
import json
import os


"""
TODO
DONE sort files by extension, move them to Extension// folder whitch is created in parallel
     maybe group similar file types like png with jpg and txt with json 
"""

DEBUG = True
# GROUPING is a boolean that decides wether files should be grouped by category
# Eg.: Images(DIR)\\funnyCat.jpg, funnierCat.png
# and not: jpg(DIR)\\funnyCat.jpg | png(DIR)\\funnierCat.png
GROUPING = True
# DIR_LOCATION is the path to the folder/directory that you'd like to organize
# Eg.: "C:\\Downloads"
DIR_LOCATION = ""
FILES_IN_DIR = os.listdir(DIR_LOCATION)


def debug(msg):
    """
    basic debug message printer\n
    only works if DEBUG is True\n
    """
    if DEBUG:
        print(msg)


def AppPairs():
    """
    Loads pairs.json into memory\n
    returns a list of lists containing the group names
    at index = 0 and the file extensions under that category\n
    """
    with open("pairs.json", "r") as f:
        appPairsList = json.loads(f.read())
    return appPairsList


def fileExtension(filename):
    """
    gets the extension of a given file by splitting it at each '.'\n
    and saving the part afer the last dot\n
    args: a valid filename\n
    returns: the the extension of given file\n
    """
    ext = filename.split(".")
    debug(f"Detected file with extension: {ext[-1]}")
    return ext[-1]


def createDir(extension):
    """
    creates a directory in DIR_LOCATION named after the extension
    argument\n
    args: a file extension to name the dir after\n
    """
    try:
        path = os.path.join(DIR_LOCATION, extension)
        os.mkdir(path)
        debug(f"SUCCESS:CREATEDIR Directory created: {path}")
    except FileExistsError:
        # a dir named as the extension might already be present
        # in that case it handles that exception
        debug(f"ERROR:CREATEDIR Directory already found: {path}")


def moveFile(fileLocation, destination):
    """
    moves files from fileLocation to destination\n
    args: fileLocation: path to a file to be moved\n
          destination: path where the file is desired to be moved\n
    """
    filename = fileLocation.split("\\")
    try:
        if not os.path.isdir(fileLocation):
            # checking wether fileLocation is a dir to avoid creating nested dirs
            shutil.move(fileLocation, destination)
            debug(f"SUCCESS:MOVEFILE {filename[-1]} moved to {destination}")
    except shutil.Error:
        debug(f"ERROR:MOVEFILE {filename[-1]} alredy present in {destination}")


def mainLoop():
    print("Organizing started")
    if not GROUPING:
        for file in FILES_IN_DIR:
            # checking each file in the given directory
            ext = fileExtension(file)
            createDir(ext)
            if not os.path.isdir(file):
                # if file is not a directory we move it
                moveFile(DIR_LOCATION+"\\"+file, DIR_LOCATION+"\\"+ext)
    else:
        #SPHAGETTI UNDER CONSTRUCTION
        for file in FILES_IN_DIR:
            ext = fileExtension(file)
            for appList in AppPairs():
                if ext in appList:
                    if not os.path.isdir(file):
                        createDir(appList[0])
                        moveFile(DIR_LOCATION+"\\"+file,
                                 DIR_LOCATION+"\\"+appList[0])
                else:
                    createDir(ext)
                    if not os.path.isdir(file):
                        moveFile(DIR_LOCATION+"\\"+file, DIR_LOCATION+"\\"+ext)
    print("Organizing finished")


mainLoop()

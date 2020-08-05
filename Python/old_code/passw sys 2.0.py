#!/usr/bin/env python3

"""
Todo
________________________________________________________________________________
[SIMPLIFIED]                Maybe make a reader app and encode entries
[CANCELLED]                 Make Login() a function
[CANCELLED]                 Make Newacc() a function
[CANCELLED_XD]              Refactor the whole thingy :)
[DONE]                      Make encdoding a function
[DONE]                      Create txt files for each user
[DONE]                      Add timestamps for each update in the user's file
[DONE]                      Separate users entries by adding date only at firs line when the day changed
[DONE]                      Make duplicate names impossible
[DONE]                      Make files and profiles removable by user
[DONE]                      Move profile files to Profiles folder in same dir as main.py
[ID]                        Add user info as number3 make it count characters, lines, number of enties and acc age
[DONE]                      Add a main loop to not quit after one task being done
For some reason adding data two or mor imes adds username_username_... date to date_check
________________________________________________________________________________
"""

import json                     #for storing users credentials
import time                     #for adding timestamps to files
import os                       #for performing os operations
import hashlib                  #for hashing passwords
import shutil                   #for moving files
import linecache                #easy way of getting specific lines from user's file
from _datetime import datetime  #for something with time
from datetime import date       #for something with time


today = date.today()
now = datetime.now()
date = today.strftime("%B %d %Y")
hrs = now.strftime("%H:%M:%S")

with open("date_file.txt", "a+") as xyz:
    pass

with open("date_file.txt", "r+") as date_file:
    date_file_data = date_file.read()

date_check = date + "XqW"

try:
    os.mkdir("user_profiles")
    print  ("Profile directory created")
except FileExistsError:
    pass

profile_dir_path = os.getcwd() + '\\user_profiles\\'

def hasher(passw):
    #This hashes whatever is given to it.
    first = passw.encode('utf-8')
    global passw1
    passw1 = hashlib.sha256(first).hexdigest()
    return passw1

with open("database.json", "a+", encoding='utf-8') as xyz:
    #Creating database and entering "{}" if empty
    dataaa = xyz.read()
    if os.stat("database.json").st_size == 0:
        xyz.write("{}")
    else:
        pass

with open("database.json", "r", encoding='utf-8') as databasefile_r:
    #Loading database and converting json to python data
    rawdata = databasefile_r.read()
    #global nevek
    nevek = json.loads(rawdata)

username = input("Enter your username: ")
user_file_path_full = profile_dir_path + username + "_Profile.txt"
if username in nevek:
    passw1 = input("Enter your password: ")
    hasher(passw1)
    if passw1 == nevek[username]:                #Checking wether the password corresponds to the username
        print(10 * "-" + "Welcome " +  username + "!" + 10 * "-")
        while True:
        #main loop. breaks when 0 is entered or when account is deleted.
            print("1 - Add data to your file.")
            print("2 - View data.")
            print("3 - View account info.")
            print("9 - Remove file with all data.")
            print("0 - Exit.")
            choice = input("Number: ")
            if choice == "0":
                print("Exiting application.")
                time.sleep(0.5)
                break
            elif choice == "1":
                new_entry = input("Enter your text: ")
                with open(user_file_path_full, "r") as reading:
                    first_line = reading.readline()
                    lenght = len(first_line)
                    line_list = reading.read()[int(lenght):].replace('\n', '')                #leaving out time of creation while checking date
                date_check = username + "_" + date_check
                if date_check in date_file_data:
                    with open(user_file_path_full, "a") as file:
                        file.write(hrs + " | " + new_entry + "\n")
                    time.sleep(0.5)
                    print("Data added to file.")
                else:
                    with open(user_file_path_full, "a") as file:
                        file.write("\n" + date + "\n" + hrs + " | " + new_entry + "\n")
                    with open("date_file.txt", "a") as date_file:
                        date_file.write(date_check + "XqW" + "\n")
                    time.sleep(0.5)
                    print("Data added to file.")
            elif choice == "2":
                with open(user_file_path_full, "r") as user_file:
                    user_file_data = user_file.readlines()[2:]
                    user_file_data = ''.join(user_file_data)
                    print(user_file_data)
            elif choice == "3":
                with open(user_file_path_full, "r") as user_file:
                    all_user_data = user_file.read()
                    foo1 = linecache.getline(user_file_path_full, 1)
                    foo2 = linecache.getline(user_file_path_full, 2)
                    two_lines = len(foo1 + foo2)
                    character_num = len(all_user_data) - two_lines
                    print("Number of characters: " + str(character_num))
                    lines_num = sum(len(line.split()) for line in open(user_file_path_full))
                    print("Number of words: " + str(lines_num))

            elif choice == "9":
                print("Are you sure you want to remove " + username + "'s profile and all of its contents? (y/n)")
                sure = input("Answer: ")
                if sure == "y":
                    os.remove(user_file_path_full)
                    del(nevek[username])
                    with open("database.json", "w", encoding='utf-8') as databasefile_w:
                        nevek = json.dumps(nevek)
                        databasefile_w.write(nevek)
                    time.sleep(0.5)
                    print("Profile removed.")
                    break
                elif sure == "n":
                    print("Cancelled.")
                else:
                    print("Invalid answer.")
            else:
                print("Invalid answer.")
    else:
        print("Access denied. Incorrect password")
else:
    while True:
        print("0 - Exit")
        print("1 - Create account with " + username + " as name.")
        print("2 - Enter new username.")
        choice_create_new_acc = input("Number: ")
        if choice_create_new_acc == "0":
            print("Exiting application.")
            time.sleep(0.5)
            break
        elif choice_create_new_acc == "1":
            newusername = username
            newpassw = input("Enter your password: ")
            newpasswcheck = input("Enter your password again: ")
            if newpassw == newpasswcheck:
                newpassw = newpassw.encode('utf-8')
                newpassw1 = hashlib.sha256(newpassw).hexdigest()              #Hashing the password
                nevek.update({newusername : newpassw1})
                data = json.dumps(nevek)
                with open("database.json", "w", encoding='utf-8') as databasefile:
                    databasefile.write(data)
                with open(newusername + "_Profile.txt", "a+") as file:
                    file.write("Account created | " + date + " " + hrs + "\n")
                with open(newusername + "_Profile.txt", "r") as file:
                    first_line = file.readline()
                    lenght = len(first_line)
                with open(newusername + "_Profile.txt", "a+") as file:
                    file.write(int(lenght) * "=" + "\n\n")
                shutil.move(newusername + "_Profile.txt", user_file_path_full)
                time.sleep(0.5)
                print("Profile added to database")
                break
            else:
                print("Passwords dont match")
        elif choice_create_new_acc == "2":
            username = input("New username: ")

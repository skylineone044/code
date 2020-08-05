from _datetime import date
from _datetime import datetime

today = date.today()
now = datetime.now()
date = today.strftime("%B %d, %Y")
time = now.strftime("%H:%M:%S")

database = open("database.txt", "a+")  # creates database.txt if not already present
database.close()

with open("database.txt", "r+") as f:  # opens the database
    users = f.read()  # sets the users variable equal to the contents of the database
    f.close()

choice = input("Dou you have an existing account? (y or n)")  # asks the user if they have a profile already
if choice == "y":  # in case if they do
    admin = input("Enter your username: ")  # asks for username
    passw = input("Enter your password: ")  # asks for password
    if admin in users:  # if the name is found in the users
        with open(admin + "Profile.txt", "r") as f:  # checks the users file
            auth = f.readline()  # sets the auth variable to the contents of the first line of the users file (admin and passw)
    else:
        print("No such profile exists.")  # if there is no file registered it breaks
    if admin in users and passw in users and admin in auth and passw in auth and admin != "" and admin != " " and passw != "" and passw != " ":  # authenticates the user by checking the database and the user's file for admin and password
        print("-" * 10 + admin + "'s profile" + "-" * 10)  # creates the header for viewing the users file
        newProfileFile = open(admin + "Profile.txt", "a+")  # opens the user's own file
        choice2 = input("Would you like to take a look at your data? (y or n)")  # asks the user wether to review their data stored in their file
        if choice2 == "y":  # if they answer yes
            newProfileFile = open(admin + "Profile.txt", "r")  # sets the newProfileFile variable equal to the contents of the users data stored in their file
            profileData = newProfileFile.readlines()[2:]  # skips the first line in the file (where login data is stored)
            profileData1 = (str(profileData).strip("[]"))  # in theory makes the list a string but does not do its job yet
            profileData2 = ''.join(profileData1)
            print("-" * 25)  # lines for aesthetics
            print(profileData2)  # prints the data stored in the profile
            print("-" * 25)  # lines for aesthetics
            choice3 = input("Would you like to add data? (y or n): ")  # asks if the user would like to add data
            if choice3 == "y":  # if they want to add data
                entry = input("Enter your text here: ")  # sets entry variable equal to the user's input
                newProfileFile = open(admin + "Profile.txt", "a")  # opens the user's file for appending
                newProfileFile.write(entry + 5 * " " + "/" + "Added: " + date + " " + time)  # writes the input into their file with timestamp
                newProfileFile.write("\n")  # adds a newline at the end of the input for aesthetics
                newProfileFile.close()  # closes the user's file
            elif choice3 == "n":  # if they don't
                newProfileFile.close()  # closes the user's file
            else:  # if the answer is not 'y' or 'n' it breaks
                print("Invalid answer. Must be y or n.")
        elif choice2 == "n":  # if they dont want to review their data
            entry = input("Enter your text here: ")  # sets entry variable equal to the user's input
            newProfileFile.write(entry + 5 * " " + "/" + "Added: " + date + " " + time)  # writes the input into their file with timestamp
            newProfileFile.write("\n")  # adds a newline at the end of the input for aesthetics
            newProfileFile.close()  # closes the user's file
        else:  # if the answer is not 'y' or 'n' it breaks
            print("Invalid answer.")
    else:
        print("Incorrect username or password.")  # if the entered username is not found in database and profile file it breaks
elif choice == "n":  # if user does not have an account
    print("You are creating a new account.\n" + "_" * 25)  # tells the user that they are creating a new account with lines for aesthetics
    newuser = input("Enter your username: ")  # asks user for username
    newpassw = input("Enter your password: ")  # asks user for password
    newpasswCheck = input("Enter your password again: ")  # asks user for password again for confirmation
    if newuser in users:  # checks if username is taken
        print("Username already taken, choose a different one.")
    else:  # if the username is not taken
        if newuser == newpassw:  # checks wether the username and password are the same
            print("Username and password can not match.")
        else:  # if username and password are different
            if newpassw == newpasswCheck:  # if the passwords match
                newProfileFile = open(newuser + "Profile.txt", "a")  # creatse the file for the user
                newProfileFile.write(newuser + " " + newpassw + "\n\n")  # adds user login details to the first line of user's file
                f = open("database.txt", "a")  # opens database
                f.write(newuser + " " + newpassw + "\n")  # adds user login details to database
                f.close()  # closes database
                print("Account added to database!")
            else:    # if the passwords do not match
                print("The given passwords dont match.")
else:  # if the answer is not 'y' or 'n' it breaks
    print("Invalid answer. Must be y or n.")

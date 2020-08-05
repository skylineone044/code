import random

file = open("file.txt", "a+")  # creates a file for the data to be stored in
randChars = ["a", "b", "c", "d"]  # list of characters to be added after each number

n = 0
while n < 100:  # makes the variable count to a hundred (one more by each 10 lines)
    n += 1
    print(str(n) + 25 * "-")  # print the number of tries (out of 100) and lines to better separate segments of the output
    file.write(str(n) + 25 * "-" + "\n")  # adding the number of tries (out of 100) and lines to better separate segments of the output to the file
    s = 0
    while s < 10:  # makes the variable count to ten (one more by each line)
        s += 1
        char = random.choice(randChars)  # getting a random character from the randChars list
        r = random.randint(0, 1)
        if r == 0:  # decides wether to make a letter uppercase or lowercase
            randChars.append(char.upper())
        else:
            randChars.append(char.lower())
        print("  " + str(s) + str(char))
        file.write("  " + str(s) + str(char) + "\n")  # adding the numbers (out of 10) and characters (chosen and made uppercase randomly) between segments to the file

file.close()

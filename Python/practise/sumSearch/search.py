"""
the premise:
    look through a set of sorted numbers and decide wether there is a pair that adds up to aspecified sum

"""

import random
n = 0
lst = []
while n < 1000:
    num = random.randint(-500, 1000)
    if num not in lst:
        lst.append(num)
    n += 1


def main():
    numList = sorted(lst)
    Sum = 1035
    i = 0
    j = -1
    first = numList[i]
    last = numList[j]
    try:
        while first + last != Sum:
            first = numList[i]
            last = numList[j]
            if first + last > Sum:
                j -= 1
            else:
                i += 1
        if first + last == Sum and first != last:
            print(str(first) + "+" + str(last) + " - found it")
        else:
            print("no matches")
    except IndexError:
        print("Sum is too big or too small")


main()

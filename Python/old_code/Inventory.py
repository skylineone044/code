import random
import json
import os

with open("inventory.json", "a+") as inv:
    if os.stat("inventory.json").st_size == 0:
        inv.write("[]")
    else:
        pass

with open("inventory.json", "r") as inv:
    raw_inv = inv.read()
    global inventory
    inventory = json.loads(raw_inv)

items = ["apple", "dirt", "diamond", "wood"]

def addToInv(item, number):
    print(inventory)
    if item in inventory:
        newNumber = inventory[item] + number
        slot = {item : newNumber}
        inventory.append(slot)
    else:
        slot = {item : number}
        inventory.append(slot)

def saveInv():
    with open("inventory.json", "w") as inv:
        data = json.dumps(inventory)
        inv.write(data)

ritem = random.choice(items)
rnumber = random.randint(1, 5)
print("you found " + str(rnumber) + " " + ritem + "(s)!")
addToInv(ritem, rnumber)
saveInv()

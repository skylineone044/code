import hashlib
import json
import os

with open("data.txt", "a+"):
	#creating txt to write text in to be encrypted
    pass

with open("encrData.json", "a+"):
	#creating json file for encrypted data to be stored in
    pass

with open("encrData.json", "a") as JFile:
	if os.stat("encrData.json").st_size == 0:
		JFile.write("[]")
		#if its empty we add brackets in it to make an empty list
	else:
		pass

with open("encrData.json", "r") as JFile:
	#reading whats stored in the hashed data
	data = JFile.read()
	lst = json.loads(data)


with open("data.txt", "r") as f:
	#reading text to be hashed
    toEncr = f.read()
    toEncr = toEncr.replace("\n", "¤")
    #replacing the newline character to make JSON work


i = 0
length = len(toEncr)
while i < length:
	#iterating through every character and hashing it
	toEncr1 = toEncr[i]
	data = toEncr1.encode('utf-8')
	doneEncr = hashlib.sha256(data).hexdigest()
	lst.append(doneEncr)
	i += 1

with open("encrData.json", "w", encoding='utf-8') as JFile:
	#saving hashed data
	data = json.dumps(lst, sort_keys=True, indent=4)
	JFile.write(data)

print("Operation succesful!")

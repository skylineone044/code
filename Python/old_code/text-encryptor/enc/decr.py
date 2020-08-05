import json

with open("decrData.txt", "a+"):
	#creating file to store the decrypted data
	pass

with open("encrData.json", "r") as JFile:
	try:
		#trying to read data to decrypt
		data = JFile.read()
		toDecr = json.loads(data)
		length = len(toDecr)
	except json.decoder.JSONDecodeError:
		#this error is thrown when nothing is in the file
		length = 0
		print("No data to decrypt!")

with open("dict.json", "r") as keys:
	#loading the hashes of the characters into memory
	data = keys.read().encode('utf-8')
	fullDict = json.loads(data)

i = 0

while i < length:
	currLine = toDecr[i]
	if currLine in fullDict:
		#if the current character is in the dict.json
		with open("decrData.txt", "a") as doneData:
			if fullDict[currLine] == "¤":
				doneData.write("\n")
				#getting \n to work properly
			else:
				doneData.write(fullDict[currLine])
				#if its not \n we write the correspondig character
	else:
		#if the caharacter is not in dict.json we write [x]
		with open("decrData.txt", "a") as doneData:
			doneData.write("[x]")
	i += 1

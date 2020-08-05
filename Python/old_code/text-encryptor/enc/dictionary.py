#This is the file used to generate dict.JSON
#This file is not meant to be opened or modified by the user

import json
import hashlib

#anything in this list is hashed and stored in dict.json
lst = " 0123456789öüóqwertzuiopőúasdfghjkléáűíyxcvbnmÖÜÓQWERTZUIOPŐÚASDFGHJKLÉÁŰÍYXCVBNM,?;.:-_*+!%/=(<)>¤"

with open("dict.json", "a+") as f:
	f.write("{")

i = 0
while i < len(lst):
	with open("dict.json", "a") as JFile:
		toEncr = lst[i]
		data = toEncr.encode('utf-8')
		doneEncr = hashlib.sha256(data).hexdigest()
		JFile.write("\"" + doneEncr + "\"" + " : " + "\"" + lst[i] + "\"" + ", \n")
		#just mess
	i += 1


with open("dict.json", "a+") as f:
	f.write("}")

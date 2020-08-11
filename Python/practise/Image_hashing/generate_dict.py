import json
import hashlib


lst = ["0","1","2","3","4","5","6","7","8","9", "[", "]", ","]

n = 0
decipher = {}
while n < len(lst):
    hashed = lst[n].encode('utf-8')
    doneHashed = hashlib.sha256(hashed).hexdigest()
    decipher.update({doneHashed : lst[n]})
    n += 1
with open("dict.json", "a+") as f:
    data = json.dumps(decipher, indent=4)
    f.write(data)

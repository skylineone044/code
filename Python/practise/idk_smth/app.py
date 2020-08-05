from clas import user
import json

with open("db.json", "r") as db:
    data = db.read()
    users = json.loads(data)


me = user("geri", "asd", "asd", users)

print(me.login(me.username, me.password, me.users))

you = user("ler", "hello", "hello", users)

you.register(you.username, you.password, you.password_check, users)

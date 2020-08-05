import json

class user:

    def __init__(self, username, password, password_check ,users):
        self.username = username
        self.password = password
        self.password_check = password_check
        self.users = users


    def login(self, username, password, users):
        # method to log the user in
        if self.password == self.users[username]:
            return True
        else:
            return False


    def update_database(self, username, password):
        # method to update the database with user's credentials
        with open("db.json", "r") as db:
            data = db.read()
            users = json.loads(data)
            users.update({self.username : self.password})
        with open("db.json", "w") as db:
            data = json.dumps(users, indent=4)
            db.write(data)


    def register(self, username, password, password_check, users):
        # method to register user and update the database with a separate method
        self.password_check = password_check
        if self.username in self.users:
            print("username already exists")
            return False
        elif self.password == self.password_check:
            user.update_database(self, username, password)
        else:
            return False

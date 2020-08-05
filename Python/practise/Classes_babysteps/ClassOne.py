class student:
    def __init__(self, name, uuid, age, isMale, gpa, major):
        self.name = name
        self.uuid = uuid
        self.age = age
        self.isMale = isMale
        self.gpa = gpa
        self.major = major

    def is_on_honor_roll(self):
        hnrll = 3.5
        if self.gpa >= hnrll:
            return True
        else:
            return False

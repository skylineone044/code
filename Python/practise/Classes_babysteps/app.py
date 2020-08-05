#from ClassOne import student
from practise.Classes_babysteps.ClassOne import student
import random
import json

randGpa = random.uniform(1.0, 5.0)
randGpa = str(randGpa)
randGpa = randGpa[:3]
randAges = random.randint(19, 25)
randNames = random.choice(["a", "b", "c", "d", "e", "f"])
majors = ["compSci", "business", "art", "engineering", "economics", "music"]
randMajors = random.choice(majors)
randIsMale = random.choice([True, False])

def generator():
    for n in range(100):
        randGpa = random.uniform(1.0, 5.0)
        randGpa = str(randGpa)
        randGpa = randGpa[:3]
        randAges = random.randint(19, 25)
        randNames = random.choice(["a", "b", "c", "d", "e", "f"])
        randMajors = random.choice(["compSci", "business", "art", "engineering", "economics", "music"])
        randIsMale = random.choice([True, False])
        with open("pupils.txt", "a+") as f:
            f.write(
                randNames + " " + str(n) + " " + str(randAges) + " " +
                str(randIsMale) + " " + str(randGpa) + " " + randMajors + "\n")


def get_data():
    bigList = []
    with open("pupils.txt", "r") as f:
        for a_line in range(100):
            raw_data = f.readline()
            xd = list(raw_data.split(" "))
            bigList.append(xd)
    return bigList


lst = get_data()
honorRoll = {}


def get_honor_roll():
    i = 0
    while i < len(lst):
        line = lst[i]
        pupil = student(line[0], int(line[1]), int(line[2]), line[3], float(line[4]), line[5])
        if pupil.is_on_honor_roll():
            major = str(pupil.major).strip()
            lista = [pupil.name, pupil.gpa, major, pupil.isMale, pupil.age]
            honorRoll.update({str(pupil.uuid): str(lista)})
        else:
            pass
        i += 1
    return honorRoll


"""
honorRoll_dict = get_honor_roll()

with open("on_honor.json", "w") as F:
    data = json.dumps(honorRoll_dict, indent=4)
    F.write(data)
"""

# please fix dis
# thank


def sort_by_major():
    j = 0
    k = 0
    srt_by_mjr = []
    while k < len(lst):
        while j < len(lst):
            clas = lst[j][5]
            # print(clas)
            # print(majors[k])
            if majors[k] in clas:
                with open("asd.txt", "a+") as f:
                    f.write(clas + "\n")
                j += 1
            else:
                j += 1
                pass
        k += 1


sort_by_major()


"""
        line = lst[j]
        pupil = student(line[0], int(line[1]), int(line[2]), line[3], float(line[4]), line[5])
        person = [pupil.major, pupil.uuid, pupil.name, pupil.gpa, pupil.isMale, pupil.age]
        srt_by_mjr.append(person)
        j += 1
    return srt_by_mjr
"""

"""
sorted_array = sort_by_major()
with open("sroted_by_major.json", "a+") as F:
    data = json.dumps(sorted_array, indent=4, sort_keys=True)
    F.write(data)
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


'''gryffendors = [
    students["name"] for student in students if students["huose"] == "Gryffendor"
]


for gryffendor in sorted(gryffendors):
    print(gryffendor) '''
    
'''def is_gryffendor(s):
    return s["house"] == "Gryffendor"

gryffindors = filter(is_gryffendor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
    
    '''
'''studentss = ["Hermione", "Harry", "Ron"]

gryffindorsdic = []

for student in studentss: 
    gryffindorsdic.append({"name": student, "house": "Gryffindor"} for student in studentss)
    
print(gryffindorsdic)'''


studentss = ["Hermione", "Harry", "Ron"]

'''gryffindors = {student: "gryffindor" for student in studentss}

print(gryffindors)'''

for i, s in enumerate(studentss):
    print(i, s)
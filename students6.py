'''with open("students.csv") as file:
    for line in file:
        student, house = line.rstrip().split(",") 
        print(f"{student} lives in {house}")'''
        
        
'''students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} lives in {house}")
        
for student in sorted(students):
    print(student)'''
    
'''students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)
        
for student in students:
    print(f"{student['name']} lives in {student['house']}")
    
        

'''
'''def get_name(student):
    return student["name"]

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)
        
for student in students:
    
    soreted_names = sorted(students, key=get_name)
    print(f"{soreted_names} lives in {student['house']}")


'''

'''def get_house(student):
    return student["name"]

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)
        
for student in students:
    
    soreted_names = sorted(students, key=get_house)
    print(f"{soreted_names} lives in {student['house']}")

'''
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)
        
for student in sorted(students, key=lambda student : student["name"]):
    
    print(f"{student["name"]} lives in {student['house']}")

'''

'''import csv


students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0]}, {"house": row[1]})
        
for student in sorted(students, key=lambda student : student["name"]):
    
    print(f"{student["name"]} lives in {student['house']}")

'''

'''import csv


students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "house": home})
        
for student in sorted(students, key=lambda student : student["name"]):
    
    print(f"{student["name"]} lives in {student['house']}")

'''

'''import csv


students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row[0], "house": row[0]})
        
for student in sorted(students, key=lambda student : student["name"]):
    
    print(f"{student["name"]} lives in {student['house']}")

'''

'''import csv 

name = input("What's your name? ")
home = input("where is your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])'''
    
import csv 

name = input("What's your name? ")
home = input("where is your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
    
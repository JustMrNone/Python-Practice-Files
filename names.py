'''
names = []
for _ in range(3):
    name = input("ellow,  what is yor name? ")
    names.append(name)

for n in sorted(names):
    print(n)'''
    
    
'''name = input()

file = open("names.txt", "w")

file.write(name)

file.close()'''

'''name = input()

file = open("names.txt", "a")

file.write(f"{name}\n")

file.close()'''

'''name = input()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")'''
    
    
#reading data from the file 


'''with open("names.txt", "r") as file:
    lines = file.readlines()
    
for _ in lines:
    print(_.rstrip())'''
    
#more compact    
'''with open("names.txt", "r") as file:
    for line in file:
        print(line.rstrip())'''
        
        
'''names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"hello, {name}")'''
    
    
with open("names.txt") as file:
    for line in sorted(file, reverse=True): 
        
        print("hello, ", line.rstrip())
'''

score = int(input("Score: "))

if 90 <= score and score <= 100:
    print("A")
elif 80 <= score and score < 90:
    print("B")
elif 70 <=score and score < 80:
    print("C")
elif 60 <= score and score < 70:
    print("D")
else: 
    print("F")
    
    
'''
#chained version 

'''

score = int(input("Score: "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <=score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else: 
    print("F") 
    
'''
#ultimateversion 
score = int(input("Score: "))

if 90 <= score:
    print("A")
elif 80 <= score:
    print("B")
elif 70 <= score:
    print("C")
elif 60 <= score:
    print("D")
else: 
    print("F")    
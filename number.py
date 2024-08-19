
'''try:
    x = int(input("what is x? "))
except ValueError:
    print("x is not an integer")
        
else:    
    print(f"x is: {x}")
finally:
    print("End of the code ")

'''

'''while True:
    try:
        x = int(input("what is x? "))
    except ValueError:
        print("x is not an integer")
    else: 
        break
print(f"x is: {x}")'''

'''while True:
    try:
        x = int(input("what is x? "))
        break
    except ValueError:
        print("x is not an integer")
print(f"x is: {x}")
'''
def main():
    integer = get_int("what's the x? ")
    print(f"x is: {integer}")

'''def get_int():
    while True:
        try:
            x = int(input("what is x? "))
        except ValueError:
            print("x is not an integer")
        else: 
            return x'''
'''def get_int():
    while True:
        try:
            x = int(input("what is x? "))
            return x
        except ValueError:
            print("x is not an integer")'''
            
'''def get_int():
    while True:
        try:
            return int(input("what is x? "))
        except ValueError:
            print("x is not an integer")'''
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass           
main()
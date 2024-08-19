def main():#main part of our function 
    variable2 = input("What's your name? ").strip().title()#we take the input and put it in a variable
    hello2(variable2)#we pass that variable to the function as the argument
    hello()
def hello():
    name = input("What's your name? ").strip().title()
    print(f"Hello, {name}")
#spliting username into first and last 
    name, last = name.split(" ")
    print("first name: ", name)
    print("last name: ", last)
#declaring a function
def hello2(variable="Name"): #variable is the parameter which have a default value of "Name"
    print(f"Hello, {variable}")#this is what function does 


main()


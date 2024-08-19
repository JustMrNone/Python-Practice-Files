def main():
    number = get_number()
    meow(number)
    
def meow(n):
    for i in range(n):
        print("Meow! ")

def get_number():
    while True:
        n = int(input("How many Meows? "))
        if n > 0:
            return n


main()

def main():
    number = getNumber()
    result = number * 100
    if result >= 99:
        print("E", end="")
    elif result <= 1:
        print("F", end="")
    else:
        print(f"{result:.0f}%")
    
def getNumber():
    while True:
        try:
            fuel, whole = input("Fraction: ").split("/")
            x, y = int(fuel), int(whole)
            if x > y or y == 0:
                continue 
        except ValueError:
            pass
        else:
            break
    return x / y


main()
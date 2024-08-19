def main():
    try:
        x = float(input("Input x:"))
        y = float(input("Input y:"))
        o = input("input operation:")
    except Exception as e:
        print(e)
    try:
        if o == "+":
            print(x + y)
        elif o == "-":
            print(x - y)
        elif o == "/":
            print(x / y)
        elif o == "*":
            print(x + y)
        else:
            print("Invalid operation")
    except Exception as e:
        print("also:", end="")
        print(e)
if __name__ == "__main__":
    main()
else:
    print("You only can run this program from main program")
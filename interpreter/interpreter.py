def main():
    x, y, z = input().split(" ")
    x, z = float(x), float(z)

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "/":
        print(x / z)
    elif y == "*":
        print(x * z)
    elif y == "**":
        print(x ** z)
        
if __name__ == "__main__":
    main()
def main():
    string = input("Greeting: ")
    print(f"${value(string)}")


def value(x):
    x = x.lower().strip()
    if x.startswith("hello"):
        return 0
    elif x.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

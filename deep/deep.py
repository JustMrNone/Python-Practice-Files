x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

match x:
    case "42" | "forty two" | "forty two":
        print("Yes")
    case _:
        print("No")
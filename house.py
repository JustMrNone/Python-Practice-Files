name = input("what is your name? ")


match name:
    case "harry" | "hermione" | "ron":
        print("griff")
    case _:
        print("not found")
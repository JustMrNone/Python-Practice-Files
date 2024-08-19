import inflect

p = inflect.engine()


my_list = []

while True:
    try:
        name = input("Name: ")
        my_list.append(name)
    except EOFError:
        print()
        break


print(f"Adieu, adieu, to {p.join(my_list)}")

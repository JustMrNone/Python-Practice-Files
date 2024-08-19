import sys

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

totalPrice = 0

while True:
    try:
        order = input("Item: ")
        order = order.title()

        for x in menu:
            if order == x:
                totalPrice += menu[x]
                print("Total: $" + format(totalPrice, '.2f'))
                break  # Stop iterating once the item is found
        else:
            continue

    except EOFError:
        print("\n")
        sys.exit(0)

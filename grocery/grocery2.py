def main():
    groceries()
def groceries():
    items = []
    basket = {}

    while True:
        try:
            item = input("")
            item = item.upper()

            items.append(item)
            items.sort()

        except EOFError:
            for item in items:
                if item not in basket:
                    basket[item] = 1
                else:
                    basket[item] += 1
            for thing in basket:
                print(str(basket[thing]) + " " + thing)
            break
        else:
            continue
main()
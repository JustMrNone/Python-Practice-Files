def main():
    price = 50
    insert = 0 
    
    while insert < price:
        print(f"Amount Due: {price - insert}")
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            insert = insert + coin
        else:
            continue
    if insert >= price:
        change = insert - price
        print(f"Change Owed: {change}")

main()
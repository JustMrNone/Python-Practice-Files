import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    if n <= 0:
        continue
    else:
        break

randomint = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess < 0:
        continue
    elif guess > randomint:
        print("Too large! ")
        continue
    elif guess < randomint:
        print("Too small! ")
        continue
    elif guess == randomint:
        print("Just right!")
        break


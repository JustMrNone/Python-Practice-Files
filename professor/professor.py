import random

def main():
    thelevel = get_level()
    score = 0
    for i in range(10):
        counter = 0
        fx, fy, sumed = generate_integer(thelevel)
        while counter < 3:

            try:
                answer = int(input(f"{fx} + {fy} = "))
            except ValueError:
                print("EEE")
                counter += 1
                continue

            if answer != sumed:
                print("EEE")
                counter += 1
                continue
            else:
                score += 1
                break
        else:
            print(f"{fx} + {fy} = {sumed}")
    print(score)


def get_level():
    while True:
        try:
            wlevel = int(input(""))
        except:
            continue
        if wlevel in [1, 2, 3]:
            return wlevel
        else:
            continue

def generate_integer(level):
    while True:
        if level == 1:
            x, y = random.randint(0, 9), random.randint(0, 9)
            return x, y, x + y
        elif level == 2:
            x, y = random.randint(10, 99), random.randint(10, 99)
            return x, y, x + y
        elif level == 3:
            x, y = random.randint(100, 999), random.randint(100, 999)
            return x, y, x + y
        else:
            raise ValueError

if __name__ == "__main__":
    main()


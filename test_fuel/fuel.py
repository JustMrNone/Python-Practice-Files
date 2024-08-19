def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            print(gauge(percentage))
            break


def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
    except ValueError:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    percentage = round((x / y) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        is_start_with_at_least_two_letter(s)
        and check_len(s)
        and is_alpha_or_is_digit(s)
        and check_first_number(s)
        and check_numbers(s)
    )


def is_start_with_at_least_two_letter(s):
    return s[0:2].isalpha()


def check_len(s):
    return 2 <= len(s) <= 6


def check_first_number(s):
    for i in range(len(s) - 1):
        if s[i].isalpha():
            if s[i + 1] == "0":
                return False
    return True



def check_numbers(s):
    for i in range(len(s) - 1):
        if s[i].isdigit():
            if not s[i + 1].isdigit():
                return False
    return True


def is_alpha_or_is_digit(s):
    for char in s:
        if not (char.isalpha() or char.isdigit()):
            return False
    return True


if __name__ == "__main__":
    main()

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not starts_with_letters(s):
        return False
    if not ends_with_numbers(s):
        return False
    if contains_invalid_characters(s):
        return False
    return True

def starts_with_letters(s):
    return s[:2].isalpha()

def ends_with_numbers(s):
    if s[-1].isdigit():
        return not any(char.isalpha() for char in s[:-1]) and s[0].isdigit() == False
    return True

def contains_invalid_characters(s):
    return any(char.isdigit() == False and char.isalpha() == False for char in s)

def main():
    plate = input("Enter the vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

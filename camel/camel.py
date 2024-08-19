def main():
    camel_case = input()
    snake_cased = spaced(camel_case).replace(" ", "_")
    print(snake_cased)
def spaced(s):
    new_string = ''
    for i, char in enumerate(s):
        if i > 0 and char.isupper():
            new_string += ' ' + char.lower()
        else:
            new_string += char
    return new_string
main()
def main():
    text = input()
    new_text = shorten(text)
    print(new_text)

def shorten(n):
    vowls = "aeiouAEIOU"
    shortend = ""

    for i in n:
        if i not in vowls:
            shortend += i + i

    return shortend

if __name__ == "__main__":
    main()

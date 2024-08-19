def main():
    x = input("Input: ")
    removed = vowl_remove(x)
    print(f"Output: {removed}")

def vowl_remove(word):
    vowls = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowls:
            result = result + char
    return result 

main()
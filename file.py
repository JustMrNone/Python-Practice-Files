
def main():
    words = input()
    vowlsre(words)

def vowlsre(word):
    
    vowls = "aeiouAEIOU"
    result = ""

    for i in word:
        if i not in vowls:
            result = result + i
    print(result)
        
if __name__ == "__main__":
    main()
def main():
    yell("this", "is", "CS50", "and", "CS50", "is", "cool")
    
def yell(*phrase):
    '''uppercase = []
    for _ in phrase:
        uppercase.append(phrase.upper())'''
    '''uppercase = map(str.upper, phrase)'''
    uppercase = [word.upper() for word in phrase]
    print(*uppercase)

if __name__ == "__main__":
    main()
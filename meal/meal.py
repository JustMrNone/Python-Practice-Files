def main():
    hour = input("What time is it? ")
    converted = convert(hour)
    if converted >= 7 and converted <= 8:
        print("breakfast time")
    elif converted >= 12 and converted <= 13:
        print("lunch time")
    elif converted >= 18 and converted <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    cnv = int(hours) + minutes
    return cnv

if __name__ == "__main__":
    main()

from datetime import datetime

while True:
    try:
        date_input = input("Date: ").strip()
        date = datetime.strptime(date_input, "%m/%d/%Y")
    except ValueError:
        try:
            date = datetime.strptime(date_input, "%B %d, %Y")
        except ValueError:
            continue
        else:
            print(f"{date.year}-{date.month:02}-{date.day:02}")
            break

    else:
        print(f"{date.year}-{date.month:02}-{date.day:02}")
        break
    


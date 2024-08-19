fruits = [
    {"fruit":"apple", "calories":130},
    {"fruit":"avocado", "calories":50},
    {"fruit":"banana", "calories":110},
    {"fruit":"cantaloupe", "calories": 50},
    {"fruit":"grapefruit", "calories": 60},
    {"fruit":"grapes", "calories": 90},
    {"fruit":"honeydew melon", "calories": 50},
    {"fruit":"kiwifruit", "calories": 90},
    {"fruit":"lemon", "calories": 15},
    {"fruit":"lime", "calories": 20},
    {"fruit":"nectarine", "calories": 60},
    {"fruit":"orange", "calories": 80},
    {"fruit":"peach", "calories": 60},
    {"fruit":"pear", "calories": 100},
    {"fruit":"pineapple", "calories": 50},
    {"fruit":"plums", "calories": 70},
    {"fruit":"strawberries", "calories": 50},
    {"fruit":"sweet cherries", "calories": 100},
    {"fruit":"tangerine", "calories": 50},
    {"fruit":"watermelon", "calories": 80},
    {"fruit":"apricot", "calories": 17},
    {"fruit":"blueberries", "calories": 85},
    {"fruit":"blackberries", "calories": 43},
    {"fruit":"cranberries", "calories": 46},
    {"fruit":"fig", "calories": 74},
    {"fruit":"guava", "calories": 68},
    {"fruit":"mango", "calories": 60},
    {"fruit":"papaya", "calories": 59},
    {"fruit":"passion fruit", "calories": 97},
    {"fruit":"persimmon", "calories": 118},
    {"fruit":"pomegranate", "calories": 83},
    {"fruit":"raspberries", "calories": 52},
    {"fruit":"blackcurrant", "calories": 63},
    {"fruit":"clementine", "calories": 35},
    {"fruit":"kiwi", "calories": 61},
    {"fruit":"lychee", "calories": 66},
    {"fruit":"mulberry", "calories": 43},
    {"fruit":"quince", "calories": 57},
    {"fruit":"star fruit", "calories": 31}
]

whichfruit = input().lower().strip()
for n in fruits: 
    fruit = n['fruit']
    colories = n['calories']
    
    if whichfruit == fruit: 
        print(f"Colories: {colories}")
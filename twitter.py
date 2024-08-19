'''url = input("Url: ").strip()

usrname = url.replace("https://twitter.com/", "")

print(url)'''

import re

url = input("Url: ").strip()

username = re.sub(r"https://twitter\.com", "", url)

print("username: ", username)
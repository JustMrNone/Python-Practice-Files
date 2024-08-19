import requests 
import sys 
import json

if len(sys.argv) != 2:
    sys.exit()
    
x = int(input("specify the number of records: "))
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={x}&term={sys.argv[1]}")


o = response.json()
for result in o["results"]:
    print(result["trackName"])
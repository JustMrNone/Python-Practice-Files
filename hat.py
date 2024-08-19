import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)
        
    

def main():
    Hat.sort("harry")
    
    
main()
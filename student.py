
class Student:
    def __init__(self, name, house):

        self.name = name 
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def house(self):
        return self._house
    #Setter
    
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
            raise ValueError
        self._house = house
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    def get(cls):
        name = input("name: ")    
        house = input("house: ")
        return cls(name, house)
'''    def charm(self):
        match self.patronus: 
            case "stag":
                return "horse emoji"
            case "Otter":
                return "po emoji"
            case "Jack Russel Terrier":
                return "dog"
            case "wolf":
                return "ayo"
            case _:
                return "You are not a wizard"'''
def main():
    
    student = Student.get()
    
    '''if student[0] == "Padma":
        student[1] = "Ravenclaw"'''
    '''if student["name"] == "Padma":
        student["house"] == "RavenClaw"    '''
            
    '''print(f'{student["name"]} from {student["house"]}')'''
    print(f'{student}')
    

'''def get_name():
    name = input("what is name? ")
    return name

def get_house():
    house = input("what is the house bitch? ")
    return house'''
    
'''def get_student():
    name = input("what is name? ")
    house = input("what is the house bitch? ")
    return [name, house]'''
    
'''def get_student():
    name = input("name: ")
    house = input("house: ")
    return {"name": name, "house": house}'''
    

#instead of dictionary we need class 

    
if __name__ == "__main__":
    main()
    


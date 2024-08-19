class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
        
class Professor(Wizard):
    def __init__(self, subject):
        self.subject = subject 
        

student = Student("harry", "gryffendor")

professor = Professor("Svereus", "asswash")

wizard = Wizard("albus")


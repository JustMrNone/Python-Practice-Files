'''MEOW = 3

for i in range(MEOW) :
    print("Moow")'''
    
    

class Cat:
    MEOWS = 3
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("Meow")
            
            

cat = Cat()
cat.meow()
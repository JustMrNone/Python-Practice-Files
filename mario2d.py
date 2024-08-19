def main():
    print_square(3)
    
def print_square(size):
    #for each row in square 
    for i in range(size):
        #for each brick in row 
        for j in range(size):    
            #print brick
            print("#", end="")
        print()
main()

def print_square(size):
    #for each row in square 
    for i in range(size):
        size = i + 1
        #for each brick in row 
        for j in range(size):    
            #print brick
            print("#", end="")
        print()
        

main()

def print_square(size):
    #for each row in square 
    for i in range(size):
        print_row(size)
        
def print_row(width):
    print("#" * width)
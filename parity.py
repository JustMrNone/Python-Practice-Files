def main():    
    x = int(input("Enter X: "))
    if iseven(x):
        print("Even")
    else:
        print("Odd")
'''
def iseven(n):
    if n % 2 == 0: 
        return True
    else:
        return False 
        
'''
#pythonic version 

def iseven(n):
    return (n % 2 == 0)
    

main()
while True:
    n = int(input())
    if n > 0:
        break
    
    
print("Meow\n" * n, end="") #pythonic

#or 

for _ in range(n):
    print("Meow")
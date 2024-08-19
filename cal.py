class Calculator:
    def __init__(self, x, y, z):
        if not x or not y or not z:
            raise ValueError("missing argument")
        self.x = x
        self.y = y
        self.z = z
        self.ans = None
        if self.y == "+":
            self.ans = self.x + self.z
        elif self.y == "-":
            self.ans = self.x - self.z
        elif self.y == "*":
            self.ans = self.x * self.z
        elif self.y == "/":
            self.ans = self.x / self.z
        elif self.y == "%":
            self.ans = self.x % self.z
        elif self.y == "**":
            self.ans = self.x ** self.z
        elif self.y == "//":
            self.ans = self.x // self.z
        else:
            raise ValueError("invalid Operation")


                
def main():
    try: 
        print(get_input())
    except ValueError:
        print("invalid input")
        return get_input()
def get_input():
    try: 
        x = int(input("first number: "))
        y = input("operation: ").strip()
        z = int(input("second number: "))
        
        calc = Calculator(x, y, z)
        answer = calc.ans
        return answer
    except ValueError:
        print("invalid input")
        return get_input()
        
if __name__ == "__main__":
    main()
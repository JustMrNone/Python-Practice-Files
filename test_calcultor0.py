from calculator import square
def main():
    test_square()
    
def test_square():
    '''for i in range(100):
        if square(i) != i * i:
            print(f"square({i}) != {i} * {i}")'''
    for i in range(-100, 101):
        try:
            assert square(i) == i * i
        except AssertionError:
            print(f"square({i}) is not", i * i, f"it returned {square(i)}")

if __name__ == "__main__":
    main()
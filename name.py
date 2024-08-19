import sys 

if len(sys.argv) < 2:
    sys.exit("please provide a name too few arguments")
for arg in sys.argv[1:]:
    print("my name is", arg)

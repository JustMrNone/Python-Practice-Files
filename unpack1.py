def f(*args, **kwargs):
    print("positional:", args)
    
def f2(*args, **kwargs):
    print("Keyword: ", kwargs)
    
    
f(1, 2, 3, 4, 6)

f2(parameter = 1, parameter1 = 2)
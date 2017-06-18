#encoding:utf-8

def Magic_calc(a, b, c=10):
    if c == 10:
        return a+b+c
    else:
        return a+b-c
        
def sum(a, b):
    return a+b
    
print Magic_calc(1, 2, 9)
import math

def radRev(a): 
    r = math.sqrt(a / math.pi)
    return r

A = float(input('원의 넓이 : '))

rad = radRev(A)
print(f"반지름의 길이 : {rad}")
import math

def triArea(b,h):
    if b < 0 or h < 0:
        a = -1
    else:
        a = 0.5 * b * h
    return a

base = float(input('삼각형의 밑변 : '))
height = float(input('삼각형의 높이 : '))

area = triArea(base,height)
print(f"삼각형의 넓이 : {area}")
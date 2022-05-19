import math

def circle_area(r):
    circleAreaValue = math.pi * r ** 2
    print(circleAreaValue)

radius = int(input("radius is "))
circle_area(radius)
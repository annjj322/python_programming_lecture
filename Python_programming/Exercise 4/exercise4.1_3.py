import math
def distance(a,b,c,d):
    x = (a - c) ** 2
    y = (b - d) ** 2
    distanceValue = math.sqrt(x + y)
    print(distanceValue)

x1 = float(input("x1 의 값을 입력하세요 : "))
y1 = float(input("y1 의 값을 입력하세요 : "))
x2 = float(input("x2 의 값을 입력하세요 : "))
y2 = float(input("y2 의 값을 입력하세요 : "))

distance(x1,y1,x2,y2)
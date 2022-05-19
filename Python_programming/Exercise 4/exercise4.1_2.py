def absolute_value(v):
    if v < 0:
        v = -v
    else:
        v = v
    print(v)

x = int(input("x의 값을 입력하세요 : "))
absolute_value(x)
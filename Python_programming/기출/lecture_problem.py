import random as rd


try:
    a = int(input("start number : "))
    b = int(input("end number : "))
except:
    print("INT ONLY")

choose_bool = False
if a <= b:
    num = rd.randint(a,b)
    print(f"choose number {a} to {b}")
else :
    temp = b
    b = a
    a = temp
    num = rd.randint(a,b)
    print(f"choose number {a} to {b}")
    
try_num = 0
while not choose_bool:
    try_num += 1
    try:
        choose_num = int(input("I guess :"))
        choose_bool = (num == choose_num)
        if choose_num < a or choose_num > b:
            print("RANGE NUMBER ONLY")
        elif choose_num < num :
            print("You are Wrong.")
            print("UP")
        elif choose_num > num :
            print("You are Wrong.")
            print("DOWN")
        print(f"TRY NUMBER : {try_num}")
    except:
        print("INT ONLY")
        
    

print(f"You are correct in {try_num} times . It's {num}.")

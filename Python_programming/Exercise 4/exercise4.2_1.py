def factorial(n):
    if isinstance(n,int) is False:
        return "ERROR. Please enter an integer"
    elif n >= 1 :
        return n * factorial(n-1)
    elif n == 0 :
        return 1
    else :
        return "ERROR. Please enter a natural number"

n = 5
ans = factorial(n)
print(ans)
# nCr = n!/{(n-r)!*r!}

def factorial(n):
    if isinstance(n,int) is False:
        return "ERROR. Please enter an integer"
    elif n >= 1 :
        return n * factorial(n-1)
    elif n == 0 :
        return 1
    else :
        return "ERROR. Please enter a natural number"

def combination(n,r):
    if n >= r:
        ans = factorial(n)/(factorial(n-r)*factorial(r))
    else :
        ans = factorial(r)/(factorial(r-n)*factorial(n))
# combination 에서 n이 r보다 작은경우는 없다.
# r을 더 크게했을 경우 n과 r의 자리를 바꾸어 준다.
    return ans        

n = 3
r = 4


ans = combination(n,r)
print(f"{n} C {r} = {ans}")
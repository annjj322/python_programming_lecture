import operator as o

opr = {'+' : o.add, '-': o.sub, '/' : o.truediv, '*' : o.mul}

def compute(num1, operator, num2):
    ans = opr[operator](num1,num2)
    return ans

n1 = 3
op = '/'
n2 = 3
ans = compute(n1,op,n2)
print(f"{n1} {op} {n2} = {ans} ")
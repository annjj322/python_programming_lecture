for a in range(1,10,1):
    for b in range(2,10,1):
        print("{0:02d}*{1:02d}={2:02d} ".format(b,a,a*b),end='')
    print('\n',end='')

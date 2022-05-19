# file name from input function
# create the file
# open write mode and save all type command before write -x command
# file.close()

fileName = input('Input the filename : ')
f = open(fileName,'w')

a = ''
while a != '-x':
    line = input('Type your input(exit: \'-x\'): ')
    if line != '-x':
        f.write(line,)
        f.write('\n')
    else:
        a = '-x'

f.close()

# isdir을 통해 폴더 이름 체크하고 현재 폴더에 포함된 모든 파일 출력
# 사용자에게 파일 이름을 받아서 파일을 출력
# 파일 이름이 다르면 다시 input 받기
# 파일 이름을 받으면 파일에 해당하는 내용을 출력

# 현재 파일의 이름을 알기 위한 작업
from glob import glob
import os
import keyword as k

cwd = os.getcwd()
print(cwd)

# python_programming 내부의 모든 폴더가 다 포함되어 있는 것을 확인
fileList = os.listdir(cwd)
print(fileList)

print('Files in the folder')
for i in fileList:
    if os.path.isfile(i) is True:
        print(i)
    else:
        pass
print('\nEnd of the file list\n')


def printFile():
    inputFile = input('Type a filename that you want to read: ')
    try: # 존재하는 파일을 입력했다면 실행
        f = open(inputFile,'r')
        global table
        table = f.read()
        f.close()
    except IndexError as e:
        print(e)

printFile()

table = table.split()
print(table)

def keywordFinder(table):
    keyDiction = {}
    for x in table:
        if k.iskeyword(x) is True: # key word인 경우 중에서도 dict value가 0이면 생성
            if x in keyDiction:
                keyDiction[x] += 1
            else:
                keyDiction[x] = 1
    for x,y in keyDiction.items():
        print(f'{x} : {y}')

keywordFinder(table)
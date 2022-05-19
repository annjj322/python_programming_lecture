# isdir을 통해 폴더 이름 체크하고 현재 폴더에 포함된 모든 파일 출력
# 사용자에게 파일 이름을 받아서 파일을 출력
# 파일 이름이 다르면 다시 input 받기
# 파일 이름을 받으면 파일에 해당하는 내용을 출력

# 현재 파일의 이름을 알기 위한 작업
import operator
import os

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
    if os.path.exists(inputFile) == True: # 존재하는 파일을 입력했다면 실행
        f = open(inputFile,'r')
        print(f.read())
        f.close()
    else:
        printFile() # try and except 문으로도 구현할 수 있지만 재귀함수 이용
        
printFile()

import random as r


def playLotto(playTime):
    randomNumSixList = []
    randomNumOneList = []
    for i in range(0,playTime):
        randomNum = list(r.sample(range(1,46),7))
        randomNumSix = randomNum[0:6]
        randomNumOne = randomNum[6:7]
        randomNumSix.sort()
        randomNumSixList.append(randomNumSix)
        randomNumOneList.append(randomNumOne)
    return randomNumSixList, randomNumOneList # list 타입으로 return
# 복수 데이터를 각각 리턴받아서 추가 기능 설정

# playTime으로 게임 실행 횟수를 받아서 함수 실행
playTime = int(input('# of lotto games: '))
play = playLotto(playTime)

for i in range(0,playTime):
    print(f'Game {i+1} Lotto numbers: {play[0][i]} Bonusnumber: {play[1][i][0]}')



# return받은 복수 데이터를 파악하기 쉽게 리스트로 저장
countingNum = []

for i in playLotto(playTime)[1]: # bonus 숫자에 해당하는 숫자만 list 에 넣음
    countingNum += i


# 각각의 데이터들의 개수를 파악해서 데이터당 빈도수를 프린트해주는 함수.
def counting(countingNum):
    n = []
    countingN = []
    for i in range(1,46):
        if countingNum.count(i) == 0:
            pass
        else:
            print("{0:02d}: {1:02d}".format(i,countingNum.count(i)))



# * 개수로 그래프 그리는 함수
def drawingGraph(countingNum):
    for t in range(0,max(countingNum)):
        for x in range(1,46):
            if countingNum.count(x) < max(countingNum)-t:
                print(' ',end='')
            elif countingNum.count(x) >= max(countingNum)-t:
                print("*",end='')
        print("")

countingSixNum = [0]
for i in playLotto(playTime)[0]:
    countingSixNum = countingSixNum + i

# 함수를 일반화했기 때문에 두가지 핵심 출력문은 따로 빼서 보기 쉽게 정리
print('------Bonus Numbers------')
counting(countingNum)
drawingGraph(countingNum)
print(123456789012345678901234567890123456789012345)


print('------Lotto Numbers------')
counting(countingSixNum) # 함수로 만들어 놓은 counting()을 다시 사용
drawingGraph(countingSixNum) # 함수로 만들어 놓은 drawingGraph()를 다시 사용
print(123456789012345678901234567890123456789012345)
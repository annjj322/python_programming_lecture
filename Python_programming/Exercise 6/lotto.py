import random as r

# 번호 45개중에서 7개의 숫자를 랜덤하게 뽑아서 List로 출력하기

def playRottery(playTime):
    countingLotto = []
    countingLottoList = []
    for i in range(0,playTime):
        randomNum = list(r.sample(range(1,46),7))
        randomNumSix = randomNum[0:6]
        randomNumOne = randomNum[6:7]
        randomNumSix.sort()
        print(f"Game {i+1} Lotto numbers: {randomNumSix} Bonus number: {randomNumOne}")
        countingLotto = countingLotto + randomNumOne 
    for n in range(1,46):
        if countingLotto.count(n) == 0:
            pass
        else:
            print("{0:02d}: {1:02d}".format(n,countingLotto.count(n)))
            countingLottoList = countingLottoList + [countingLotto.count(n)] # maximum number를 구하기 위한 list
    # maximum 값을 고정시키고 *을 for문으로 반복 출력

    for t in range(0,max(countingLottoList)):
        for x in range(1,46):
            if countingLotto.count(x) < max(countingLottoList)-t:
                print(' ',end='')
            elif countingLotto.count(x) >= max(countingLottoList)-t:
                print("*",end='')
        print("")
    


# 사용자가 입력한 숫자만큼 게임 실행

playTime = int(input("# of Lotto games: "))
playRottery(playTime)

print("123456789012345678901234567890123456789012345")
second = 1
minute = 60 * second
hour = 60 * 60 * second
# 계산하기 쉽게 단위를 통일

startTime = 0 * second + 52 * minute + 6 * hour
# 기준이 되는 시각을 초단위로 변형

oneMilePace = 8 * minute + 15 * second
secondMilesPace = 7 * minute + 12 * second
# 3miles
lastMilesPace = oneMilePace
# 더해 주어야하는 시간을 전부 초단위로 변형

secondMilesNumber = 3
# 두번째 구간의 곱해주어야 하는 마일 수

breakfastTime = (startTime + oneMilePace + secondMilesPace * secondMilesNumber + lastMilesPace)
# 초로 변형한 시각에 모든 구간에서 걸리는 시간을 더함

breakfastTimeHours = int(breakfastTime / 3600)
# 초를 3600으로 나눈 몫은 시간이 됨
breakfastTimeMinutes = int((breakfastTime % 3600) / 60)
# 시간이 되고 남은 나머지를 60으로 나눈 몫이 됨
breakfastTimeSeconds = (breakfastTime % 3600) % 60
# 분이 되고 남은 나머지를 60으로 나눈 나머지가 초가 됨
# 초단위로 더해져 있는 시간을 역으로 변형시키는 원리

print(f"It  was  {breakfastTimeHours}  :  {breakfastTimeMinutes}  :  {breakfastTimeSeconds}  when  I  got  home  for  breakfast")
# 나누어 정리해둔 시간과 분 초를 답에 맞게 노출
# 변수와 str을 같이 쓰는 방법 사용

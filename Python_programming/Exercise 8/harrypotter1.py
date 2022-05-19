f = open('harrypotter.txt')
harryPotter = f.read()
word = harryPotter.split()

emptyList = []
countingList = []

for i in word:
    if word.count(i) >= 2:
        print(i)
        if i not in emptyList:
            print(i)
            emptyList.append(i)
            countingList += str(word.count(i))

print(emptyList)
print(countingList)

for i in range(0,len(emptyList)):
    print(f"{emptyList[i]} : {countingList[i]}")


f.close

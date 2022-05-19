from anyio import DelimiterNotFound


cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)

mix = [cheeses, numbers, empty]
print(mix)

age = 30
mix2 = [cheeses, numbers, empty, age, 0.5*age, 0.5]
print(mix2)


numbers[1] = 5
print(numbers)

cheeses = ['Cheddar','Edam','Gouda']
print('Gouda' in cheeses)
print('GOUDA' in cheeses)
print('Gouda' not in cheeses)

for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers = numbers * 2

for x in []:
    print('This never hapens')
    
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

thislist = ['apple','banana','cherry']
thislist = thislist.append('orange')
print(thislist)

thislist.insert(1,'melon')
print(thislist)

fruits = ['apple','banana','cherry']
cars = ['Ford', 'BMW','Volvo']
fruits.extend(cars)
print(fruits)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars[2] = 'bmw'

print(cars)

fruits.reverse()
print(fruits)

x = fruits.count('cherry')
print(x)

x = fruits.index('cherry')
print(x)

thislist.remove('banana')
print(thislist)

thislist.pop()
print(thislist)

thislist.pop(0)
print(thislist)

thislist.clear()
print(thislist)

thislist = ['apple','banana','cherry']
del thislist[0]
print(thislist)

s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)

s = 'spam-spam-spam'
div = '-'
t = s.split(div)
print(t)

t = ['pining','for','the','fjords']
delimiter = ' '
s = delimiter.join(t)
print(s)

listA = [a,b,c]
listB = [a,b,c]
print(listA is listB)

a = 'a'
b = 'a'
a is b
# True

a = 'banana'
b = a
print(a is b)
b = 'apple' 
print(a)
print(a is b)




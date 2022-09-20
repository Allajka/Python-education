numbers = [1, 2, 3, 4, 5]
print(numbers) 

numbers = range(1, 6)
print(type(numbers)) 

numbers = list(range(1, 6)) #приведение к типу list
print(type(numbers)) 
print(numbers) 

numbers[0] = 10 #замена нулевого элемента
print(numbers) # [10, 2, 3, 4, 5]

print(f"{len(numbers)} len") # размер

for i in numbers: #так мы не заменяем а просто выводим
 i *= 2
 print(i) 
print(numbers) 

colors = ['red', 'green', 'blue']

for e in colors:
    print(e) #red green blue

for e in colors:
    print(e*2) #redred greengreen blueblue

colors.append('gray') #добавить в конец списка
print(colors == ['red', 'green', 'blue', 'gray']) #True
colors.remove('red') #удалить 'red'
del colors[0] #удалить элемент
print(colors)
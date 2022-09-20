original = 23
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
print(inverted)

original = 23
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
else:
 print('Пожалуй')
 print('хватит )')
print(inverted)

for i in 1,2,3,4:
    print(i**2)

numbers = [2, 5, 7]
for i in numbers:
    print(i**2)   

list = range(5) # от 0 до 4
for i in list:
    print(i)  

for i in range(2, 6):  # от 2 до 5
    print(i)  

for i in range(2, 10, 2):  # от 2 до 9 увеличивая на 2
    print(i)  

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
for c in text:
    print(c)

help(text.find())
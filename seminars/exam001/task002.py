#Найти максимальное из пяти чисел

# list = [2, 8, 9, 12]
# print(max(list))

size = int(input("Введите размер списка: "))
list = []
for i in range(0,size):
    number = int(input("Введите число: "))
    list.append(number)
max = list[0]

for i in range(1, len(list)):
    if max < list[i]:
        max = list[i]
print(list)
print(f"Max = {max}")
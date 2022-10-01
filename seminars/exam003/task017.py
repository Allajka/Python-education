# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

n = 8
numbers = []
for i in range(-n, n + 1):
    numbers.append(i)
print(numbers)

with open('file.txt', 'w') as data:
    data.write("1\n")
    data.write("3\n")
    data.write("hdjfh")

path = 'file.txt'
data = open(path, 'r')
total = 1
for line in data:
    if line.isdigit():
        if int(line) <= len(numbers):
            total *= numbers[int(line)]
data.close()

print(total)


# numbers = int(input("Введите число N: "))
# n = list(range(-numbers, numbers+1))
# print(n, end = ' ')
#
# path = 'text.txt'
# data = open(path, 'r')
# datalist = [int(line.strip()) for line in data]
# print('\n',datalist)
# data.close()
#
# mult = 1
# for i in datalist:
#     mult *= n[i]
#
# print(mult)
# Напишите программу, в которой пользователь вводит целое число, а программа определяет, сколько в этом числе
# цифр 0, 1, 2 и т.д до 9
number = input('Введите число: ')
numbers = [int(i) for i in number]
print(numbers)

for i in range(10):
    counted = 0
    for j in numbers:
        if i == j:
            counted += 1
    print(f'{i} в числе {int(number)} присутствует {counted} раз ')

# for i in numbers:
#     counted = 0
#     for j in numbers:
#         if i == j:
#             counted += 1
#     print(f'{i} в числе {int(number)} присутствует {counted} раз ')

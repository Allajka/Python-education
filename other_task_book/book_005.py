# Напишите программу, в которой описана функция, возвращающая результатом сумму нечетных чисел. Кол-во чисел передается аргументом функции

def Sum_uneven(list_number):
    sum_number = 0
    for i in range(0, len(list_number)):
        if list_number[i] % 2 == 1:
             sum_number += list_number[i]
    return sum_number

from random import randint
numbers = [randint(1, 100) for i in range(5)]
print(numbers)

print(f"Сумма сумму нечетных чисел из списка равна: {Sum_uneven(numbers)}")

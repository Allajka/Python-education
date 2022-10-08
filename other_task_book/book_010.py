# Пользователь вводит три числа, а программа проверяет, являются ли эти числа арифметической последовательностью.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
numbers = [a, b, c]
numbers = sorted(numbers)
print('YES' if numbers[1]-numbers[0] == numbers[2] - numbers[1] else "NO")
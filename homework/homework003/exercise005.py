# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import functions as fun

print('Программа выводит последовательность чисел Фибоначчи от -n до n.')
n = abs(fun.check_input_number('Введите n: '))
fibonacci = []
for i in range(-n, n + 1):
    fibonacci.append(fun.fibonacci(i))
print(fibonacci, end='')

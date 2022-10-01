# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

import functions as fun

numbers = fun.create_list_number_random(9)
print(numbers)
multiplication = 1
if len(numbers) % 2 == 0:
    for i in range(len(numbers) // 2):
        multiplication = numbers[i] * numbers[len(numbers) - i - 1]
        print(f'{numbers[i]} * {numbers[len(numbers) - i - 1]} = {multiplication}')
else:
    for i in range(len(numbers) // 2):
        multiplication = numbers[i] * numbers[len(numbers) - i - 1]
        print(f'{numbers[i]} * {numbers[len(numbers) - i - 1]} = {multiplication}')
    multiplication = numbers[len(numbers) // 2] * numbers[len(numbers) // 2]
    print(f'{numbers[len(numbers) // 2]} * {numbers[len(numbers) // 2]} = {multiplication}')

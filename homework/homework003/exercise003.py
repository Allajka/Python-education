# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import functions as fun

numbers = fun.create_list_number_float_random(5)
print(numbers)
largest = 0
smallest = int(str(numbers[0]).split('.')[1])

for i in numbers:
    if int(str(i).split('.')[1]) > largest:
        largest = int(str(i).split('.')[1])
    if int(str(i).split('.')[1]) < smallest:
        smallest = int(str(i).split('.')[1])

print(f'Максимальное значение дробной части элементов {largest / 1000}')
print(f'Минимальное значение дробной части элементов {smallest / 1000}')
print(f'Разница {(largest - smallest) / 1000}')
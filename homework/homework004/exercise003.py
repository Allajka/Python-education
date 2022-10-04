# 3) Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Если в первом списке число повторялось, добавлять его не нужно.
# Вариант со словарями
list_numbers = [1, 1, 2, 3, 4, 4, 5, 1, 3, 8, 6, 5, 5, 10]

dictionary_list_numbers = {}

for numbers in list_numbers:
    dictionary_list_numbers.setdefault(numbers, 0)
    if numbers in dictionary_list_numbers:
        dictionary_list_numbers[numbers] = dictionary_list_numbers[numbers] + 1

print(dictionary_list_numbers)

unique_list_numbers = []

for key, value in dictionary_list_numbers.items():
    if value == 1:
        unique_list_numbers.append(key)

print(unique_list_numbers)

# 3) Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Если в первом списке число повторялось, добавлять его не нужно.

# Через map(для ввода) + filter + count
converted_list = list(map(int, input('Введите список элементов через пробел: ').split()))
filtered_list = list(filter(lambda x: converted_list.count(x) == 1, converted_list))
print(filtered_list)


# Через List Comprehension
converted_list = list(map(int, input().split()))
filtered_list = [x for x in converted_list if converted_list.count(x) == 1]
print(filtered_list)


# С использованием функции count()
# user_numbers = list(map(int, input('Введите список элементов через пробел: ').split()))
# user_list = input('Введите список элементов через пробел: ').split()
# unique_list = []
#
# for i in user_list:
#     if user_list.count(i) == 1:
#         unique_list.append(i)
#
# print(user_list)
# print(unique_list)


# Через цикл
# user_list = list(input('Введите список элементов через пробел: ').split())
# unique_list = []
#
# for i in user_list:
#     count = 0
#     for j in user_list:
#         if i == j:
#             count += 1
#     if count == 1:
#         unique_list.append(i)
# print(unique_list)


# Вариант со словарями
# list_numbers = [1, 1, 2, 3, 4, 4, 5, 1, 3, 8, 6, 5, 5, 10]
#
# dictionary_list_numbers = {}
#
# for numbers in list_numbers:
#     dictionary_list_numbers.setdefault(numbers, 0)
#     if numbers in dictionary_list_numbers:
#         dictionary_list_numbers[numbers] = dictionary_list_numbers[numbers] + 1
#
# unique_list_numbers = []
#
# for key, value in dictionary_list_numbers.items():
#     if value == 1:
#         unique_list_numbers.append(key)
#
# print(unique_list_numbers)

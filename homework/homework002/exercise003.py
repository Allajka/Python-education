# Задайте список (словарь не нужно выводить!) из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Через Dict Comprehension
d = {n: 3*n+1 for n in range(1, 10)}
print(d)


# print("Программа создает список из n чисел последовательности по формуле: (1+1/n)^n.")
# number = int(input("Введите n: "))
#
# list_number = [((1+1/i)**i) for i in range(1, number+1)]
# print(F"Последовательность: {list_number}")
#
# sum_numbers = 0
# for i in range(0, len(list_number)):
#     sum_numbers += list_number[i]
# print(f"Сумма чисел последовательности = {sum_numbers}")

# Вариант с округлением до 3 чисел после запятой
# print("Программа создает список из n чисел последовательности по формуле: (1+1/n)^n.")
# number = int(input("Введите n: "))

# list_number = [round(((1+1/i)**i), 3) for i in range(1, number+1)]
# print(F"Последовательность: {list_number}")

# sum_numbers = 0
# for i in range(0, len(list_number)):
#     sum_numbers += list_number[i]
# print(f"Сумма чисел последовательности = {sum_numbers}")

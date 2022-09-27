# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

print("Программа определяет сумму цифр в числе.")
numbers = list(input("Введите число: "))
sum_numbers = 0

for i in range(0, len(numbers)):
    if numbers[i] != "." and numbers[i] != "-":
        sum_numbers += int(numbers[i])

print(f"Сумма цифр числа {sum_numbers}")

# Вариант с функцией и строкой
# def Sum_number(number):
#     number = number.replace(',', '')
#     number = number.replace('.', '')
#     number = number.replace('-', '')
#     number = int(number)
#     sum = 0
#     while number > 0:
#         sum += number % 10
#         number //= 10
#     return sum

# print("Программа определяет сумму цифр в числе.")
# user_number = input("Введите ваше число: ")
# print(f"Сумма цифр в числе {user_number} = {Sum_number(user_number)}")
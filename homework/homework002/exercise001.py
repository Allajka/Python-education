# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

numbers = list(input("Введите число: "))
sum_numbers = 0

for i in range(0, len(numbers)):
    if numbers[i] != "." and numbers[i] != "-":
        sum_numbers += int(numbers[i])

print(f"Сумма цифр числа {sum_numbers}")
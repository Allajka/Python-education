# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.

number = int(input())
number1 = number // 1000
number2 = (number // 100) % 10
number3 = (number // 10) % 10
number4 = number % 10
if number1 + number4 == number2 - number3:
    print("ДА")
else:
    print("НЕТ")

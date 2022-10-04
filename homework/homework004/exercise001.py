# 1) Вычислить число π c заданной точностью d
# Пример:при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

# Итоговый вариант: Алгоритм Чудновского π(количество знаков после запятой от 1 до 26)
import functions as fun
from decimal import *

print("Программа показывает число π c заданной точностью.")
symbol_comma = abs(fun.check_input_number('Введите количество знаков после запятой для вывода числа π(от 1 до 26): '))
while symbol_comma > 26:
    print('Введено не верное значение. Повторите ввод.')
    symbol_comma = abs(
        fun.check_input_number('Введите количество знаков после запятой для вывода числа π(от 1 до 26): '))

number_pi = Decimal(0)
for i in range(2):
    number_pi += (Decimal(-1) ** i) * (Decimal(fun.factorial(6 * i))) / (
            (fun.factorial(i) ** 3) * (fun.factorial(3 * i))) * (13591409 + 545140134 * i) / (640320 ** (3 * i))
number_pi = number_pi * Decimal(10005).sqrt() / 4270934400
number_pi = number_pi ** (-1)
number_pi_format = round(number_pi, symbol_comma)
print(number_pi_format)


# Вариант Алгоритм Чудновского π(количество знаков после запятой от 1 до 15)
# import functions as fun
#
# print("Программа показывает число π c заданной точностью.")
# symbol_comma = abs(fun.check_input_number('Введите количество знаков после запятой для вывода числа π(от 1 до 15): '))
# while symbol_comma > 15:
#     print('Введено не верное значение. Повторите ввод.')
#     symbol_comma = abs(
#         fun.check_input_number('Введите количество знаков после запятой для вывода числа π(от 1 до 26): '))
#
# number_pi = 0
# for i in range(2):
#     number_pi += (-1) ** i * fun.factorial(6 * i) * (13591409 + 545140134 * i) / (
#             fun.factorial(3 * i) * fun.factorial(i) ** 3 * (640320 ** 3) ** (i + 1 / 2))
# number_pi = (12 * number_pi) ** (-1)
#
# number_pi_format = round(number_pi, symbol_comma)
# print(number_pi_format)


# Вариант вычисления числа Пи через ряд Нилаканта, 10 верных знаков после запятой
# print("Программа показывает число π c заданной точностью.")
# symbol_comma = abs(fun.check_input_number('Введите количество знаков после запятой для вывода числа π(от 1 до 10): '))
# while symbol_comma > 10:
#     print('Введено не верное значение. Повторите ввод.')
#     symbol_comma = abs(
#         fun.check_input_number('Введите количество знаков после запятой для вывода числа π(от 1 до 10): '))
#
# pi = 3.0
# sign = 1
#
# for i in range(2, 3000, 2):
#     pi += (4 * sign) / (i * (i + 1.0) * (i + 2.0))
#     sign = -sign
#
# pi_format = round(pi, symbol_comma)
# print(pi_format)

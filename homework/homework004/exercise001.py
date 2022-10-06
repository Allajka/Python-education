# 1) Вычислить число π c заданной точностью d
# Пример:при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import functions as fun

print('Программа выведет число π с определенной точностью.')
user_number = input('Формат ввода: 0.001 -> покажет 3 цифры после запятой.\nВведите значение: ')
size = abs(len(user_number) - user_number.find('.') - 1)
pi = 0
for i in range(size):
    pi += (1 / 16 ** i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))

print(str(pi)[:len(user_number)])

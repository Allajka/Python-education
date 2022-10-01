# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101; 3 -> 11; 2 -> 10
import functions as fun

user_number = fun.check_input_number('Введите целое число: ')
save_number = user_number
binary_number = 0
ten = 1

while abs(user_number) > 0:
    binary_number += (abs(user_number) % 2) * ten
    user_number = abs(user_number) // 2
    ten *= 10

if save_number > 0:
    print(int(binary_number))
elif save_number < 0:
    print(-int(binary_number))

# Вариант со строкой
# user_number = fun.check_input_number('Введите целое число: ')
# save_number = user_number
# binary_number = ''
# user_number = abs(user_number)
# while user_number > 0:
#     if user_number % 2 == 0:
#         binary_number = '0' + binary_number
#     else:
#         binary_number = '1' + binary_number
#     user_number //= 2
#
# if save_number > 0:
#     print(int(binary_number))
# elif save_number < 0:
#     print(-int(binary_number))

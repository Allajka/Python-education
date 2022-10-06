# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import functions as fun


def simple_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True


def create_simple_list(last_Number):
    simple_list = [2]
    for i in range(3, last_Number+1, 2):
        if simple_number(i):
            simple_list.append(i)
    return simple_list


def return_simple_multiplication_number(number, simple_list):
    result = f"{number} = 1"
    i = 0
    while i < number:
        if number % simple_list[i] == 0:
            number /= simple_list[i]
            result = f"{result} * {simple_list[i]}"
            i = 0
        else:
            i += 1
    print(result)


user_number = abs(fun.check_input_number('Введите целое положительное число: '))
simple_list = create_simple_list(user_number)
if user_number == 0:
    print(f"Введен 0.")
elif user_number in simple_list:
    print(f"{user_number} = 1 * {user_number}")
else: return_simple_multiplication_number(user_number, simple_list)
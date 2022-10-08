def create_list_number_random(size):
    from random import randint
    list_number = [randint(1, 100) for _ in range(size)]
    return list_number


def create_list_number_float_random(size):
    import random
    list_number = [round(random.uniform(0, 20), 3) for _ in range(size)]
    return list_number


def check_input_number(text):
    flag = False
    while flag == False:
        user_number = input(text)
        try:
            float(user_number)
            return int(user_number)
        except ValueError:
            flag == False

def fibonacci(n):
    if n > 0:
        if n in [1, 2]:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    elif n < 0:
        if n in [-1, -2]:
            return -1
        else:
            return fibonacci(n + 1) - (-fibonacci(n + 2))
    elif n == 0:
        return 0

def negafibonacci(number):
    if number in [1, 2]:
        return 1
    if number < 0:
        return negafibonacci(-number) * (-1) ** (-number + 1)
    else:
        return negafibonacci(number - 1) + negafibonacci(number - 2)
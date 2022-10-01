# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_list_number_input(size):
    print(f'Введите {size} чисел, каждое число вводится через enter.')
    list_number = []
    while size > len(list_number):
        user_number = input('Введите число: ')
        flag = user_number.isdigit()
        if flag:
            list_number.append(int(user_number))
    return list_number


def create_list_number_random(size):
    from random import randint
    list_number = [randint(1, 100) for _ in range(size)]
    return list_number


print('Программа, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')
size_list = int(input('Введите размер списка: '))
user_answer = input('''Если вы хотите ввести список самостоятельно введите - да
Если вы хотите, создать список автоматически введите - нет.
Ваш ответ: ''')

if user_answer.lower() == 'да':
    numbers = create_list_number_input(size_list)
elif user_answer.lower() == 'нет':
    numbers = create_list_number_random(size_list)

total = 0
print(numbers)
for i in range(1, len(numbers), 2):
    total += numbers[i]
print(f'Сумма элементов списка, стоящих на нечётных позициях: {total}')

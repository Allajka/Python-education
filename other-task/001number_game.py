# from random import randint
#
# left, right = 1, 100
# middle = (left + right) // 2
# count = 0
# num = randint(left, right)
# while middle != num:
#     if middle > num:
#         right = middle - 1
#         middle = (left + right) // 2
#         count += 1
#     elif middle < num:
#         left = middle + 1
#         middle = (left + right) // 2
#         count += 1
# print(f'Количество попыток: {count}, это число: {middle}')

# За какое наименьшее количество вопросов можно гарантированно угадать число от 1 до n
# from math import *
# n = int(input())
# print(ceil(log2(n)))

# Угадайка чисел

from random import *


def check_input(start, end, text):
    number = input(text)
    if number.isdigit() and start <= int(number) <= end:
        return int(number)
    else:
        print(f"Ошибка ввода, попробуйте еще раз ввести число от {start} до {end}.")
        check_input(start, end, text)


def game(start, end, answer):
    count = 0
    while True:
        user_answer = check_input(start, end, "Ваш ответ: ")
        count += 1
        if user_answer < answer:
            print('Ваше число меньше загаданного, попробуйте еще раз')
        elif user_answer > answer:
            print('Ваше число больше загаданного, попробуйте еще раз')
        else:
            print(f'Вы угадали!!! Количество попыток: {count}. Загаданное число: {answer}')
            break


def start_game():
    start, end = 1, int(input("Вы хотите угадывать число от 1 до (введите число):"))
    answer = randint(start, end)
    return start, end, answer


def next_actions():
    while True:
        print('Если хотите сыграть еще раз напишите "да", для выхода напишите "выход"')
        decision = input().lower()
        if decision.isalpha() and decision == "да":
            start, end, answer = start_game()
            game(start, end, answer)
        elif decision.isalpha() and decision == "выход":
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        else:
            print('Что-то пошло не так, повторите ввод.')


print(f'Добро пожаловать в числовую угадайку.')
start, end, answer = start_game()
game(start, end, answer)
next_actions()

# Генератор безопасных паролей
from random import *

def generator_password(size):
    password = ''
    while len(password) != size:
        if answer_numbers:
            password += str(choice(DIGITS))
        if len(password) == size: break
        if answer_lower:
            password += choice(LOWERCASE_LETTERS)
        if len(password) == size: break
        if answer_upper:
            password += choice(UPPERCASE_LETTERS)
        if len(password) == size: break
        if answer_chars:
            password += choice(PUNCTUATION)
        if len(password) == size: break
    return password

def check_number(text):
    number = input(text)
    if number.isdigit():
        return int(number)
    else:
        print("Ошибка, повторите ввод.")
        check_number(text)

def check_answer(text):
    answer = input(text).lower()
    if answer.isalpha() and answer == 'да':
        return True
    elif answer.isalpha() and answer == 'нет':
        return False
    else:
        print("Ошибка, повторите ввод.")
        check_answer(text)



DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

amount = check_number('Какое количество паролей нужно создать, введите цифру: ')
size = check_number('Какое длинна паролей, введите цифру: ')
while True:
    answer_numbers = check_answer("Включать ли цифры(напишите да или нет)?")
    answer_lower = check_answer("Включать ли прописные буквы(напишите да или нет)?")
    answer_upper = check_answer("Включать ли строчные буквы(напишите да или нет)?")
    answer_chars = check_answer("Включать ли символы(напишите да или нет)?")
    if answer_numbers or answer_lower or answer_upper or answer_chars:
        break
    else:
        print('Эм... А из чего будем создавать пароль? Нужно что-то выбрать.')


for _ in range(amount):
    print(generator_password(size))

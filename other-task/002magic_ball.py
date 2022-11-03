# Магический шар
# from random import *
# answers = [
#     "Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
#     "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
#     "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
#     "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
#     "Перспективы не очень хорошие", "Весьма сомнительно"
# ]
# print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
# name = input('Как тебя зовут? ')
# while True:
#     question = input(f'{name} задай свой вопрос: ')
#     if not question == "":
#         print(f'Ответ: {choice(answers)}')
#     decision = input(f'{name} остались ли у тебя ещё вопросы ко мне?(напиши да или нет)').lower()
#     if decision == 'нет':
#         print('Возвращайся если возникнут вопросы!')
#         break

import random, time
from colorama import Fore, Back, Style
from colorama import init

init()

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай!!!",
           "Предрешено", "Вероятнее всего...", "Спроси позже, не получилось", "Мой ответ - нет!",
           "Никаких сомнений!", "Да, здесь хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можете быть уверены в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print(Fore.CYAN)
privet= ' 🔮 Привет, я магический шар...  '
for i in privet:
    time.sleep(0.10)
    print(i,end='')
time.sleep(2)
print('\nи я знаю ответ на любой твой вопрос...')
time.sleep(2)
print(Fore.RESET)

name = input('Как тебя зовут, я тоже знаю :-),  можешь просто написать никнейм свой:\n\n')


restart = 'y'
while restart == 'y':
    colortext = [Fore.CYAN, Fore.RED, Fore.BLUE, Fore.WHITE, Fore.MAGENTA, Fore.GREEN]
    print(name + ", отлично! Поехали через...")
    print(random.choice(colortext), end='')
    print(' '*(10+len(name))+'3')
    time.sleep(1)
    print(random.choice(colortext), end='')
    print(' '*(10+len(name))+'2')
    print(random.choice(colortext), end='')
    time.sleep(1)
    print(' '*(10+len(name))+'1')
    print(Style.RESET_ALL, end='')

    q = input('Задавай вопрос, жми ENTER и жди ответа...:\n')
    sec = random.randint(1, 5)
    time.sleep(sec)
    print()
    ch = random.choice(answers)
    char = ['☯', '✓', '立', '☺', '◒', '☼', '༓','✪','◮','▒','░']
    POLOSA = random.choice(char) * len(ch)
    print(POLOSA)
    print(ch)
    print(POLOSA)
    while True:
        time.sleep(3)
        print(random.choice(colortext))
        restart = input('Хочешь задать ещё вопрос?: \n')
        print(Style.RESET_ALL, end='')
        if restart in ['n','no','нет','не','not','exit']:
            time.sleep(1)
            print(Fore.CYAN)
            print('Ok, возвращайся если возникнут вопросы!')
            time.sleep(3)
            break
        else:
            restart = 'y'
        break
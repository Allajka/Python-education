# b) Подумайте как наделить бота "интеллектом"
# Алгоритм:
# 1. игроку предлагается выбрать первым или вторым он будет ходить.
# 2. Компьютер может пойти рандомно по двум веткам - верный алгоритм или любое рандомное число.
# 3. Так же компьютер выводит 3 варианта сообщений в зависимости от ветки(правильной или не правильной).
# 4. Таким образом у игрока есть шанс победить.

from random import randint
def control_input(control_number, text):
    flag = False
    while flag == False:
        user_number = input(text)
        try:
            user_number = int(user_number)
            if 0 < user_number <= control_number:
                flag = True
                return int(user_number)
        except ValueError:
            flag == False

print('На столе лежит 101 конфета. Вы играете против компьютера.\nЗа один ход можно забрать не более чем 28 конфет.\n')
move = control_input(2, f'Вы хотите ходить первым или вторым? Введите ваш вариант цифрой: ')

candies = 101
control_candies = 28
if move == 1:
    print('Ваш ход будет первым. \n   \033[1mИгра началась \033[0m')
    while candies > 0:
        player = control_input(control_candies, f'На столе лежит \033[1m{candies}\033[0m конфета. \033[1mВаш ход: \033[0m')
        candies -= player
        if candies <= 0:
            print('\n🎉🎉🎉 Вы победили 🎉🎉🎉')
            break

        lottery = randint(1, 2)
        if lottery == 1:
            computer = candies % (control_candies+1)
        else:
            computer = randint(1, 28)
        print(f'На столе лежит \033[1m{candies}\033[0m конфета. Компьютер в свой ход забрал \033[1m{computer}\033[0m конфет.')
        candies -= computer
        if candies <= 0:
            print('\nВас обыграл компьютер 😒\nПопробуйте еще!')
            break

        answer = randint(1, 3)
        if not candies % (control_candies+1) == 0:
            if answer == 1:
                print("\033[1mкомпьютер:\033[0m Ой, кажется я не туда нажал.")
            elif answer == 2:
                print("\033[1mкомпьютер:\033[0m Что-то я себя не важно чувствую.")
            else:
                print("\033[1mкомпьютер:\033[0m У тебя есть реальные шансы победить.")

        if candies % (control_candies+1) == 0:
            if answer == 1:
                print("\033[1mкомпьютер:\033[0m Соберись! Я уже чувствую вкус победы.")
            elif answer == 2:
                print("\033[1mкомпьютер:\033[0m Ты точно хочешь победить?")
            else:
                print("\033[1mкомпьютер:\033[0m Пам-пам, я уже потираю ручки.")
else:
    print('Ваш ход будет вторым. \n   \033[1mИгра началась \033[0m')
    while candies > 0:
        computer = candies % (control_candies + 1)
        print(f'На столе лежит \033[1m{candies}\033[0m конфета. Компьютер в свой ход забрал \033[1m{computer}\033[0m конфет.')
        candies -= computer
        answer = randint(1, 3)
        if not candies % (control_candies+1) == 0:
            if answer == 1:
                print("\033[1mкомпьютер:\033[0m Ой, кажется я не туда нажал.")
            elif answer == 2:
                print("\033[1mкомпьютер:\033[0m Что-то я себя не важно чувствую.")
            else:
                print("\033[1mкомпьютер:\033[0m У тебя есть реальные шансы победить.")

        if candies % (control_candies+1) == 0:
            if answer == 1:
                print("\033[1mкомпьютер:\033[0m Соберись! Я уже чувствую вкус победы.")
            elif answer == 2:
                print("\033[1mкомпьютер:\033[0m Ты точно хочешь победить?")
            else:
                print("\033[1mкомпьютер:\033[0m Пам-пам, я уже потираю ручки.")


        if candies <= 0:
            print('\nВас обыграл компьютер 😒\nПопробуйте еще!')
            break
        player = control_input(control_candies, f'На столе лежит \033[1m{candies}\033[0m конфета. \033[1mВаш ход: \033[0m')
        candies -= player
        if candies <= 0:
            print('\n🎉🎉🎉 Победил первый игрок 😎')
            break
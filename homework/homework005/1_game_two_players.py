# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.

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


candies = 101
control_candies = 28

print('На столе лежит 101 конфета. Играют два игрока делая ход друг после друга.\nЗа один ход можно забрать не более чем 28 конфет.\n')
lottery = randint(1, 2)

if lottery == 1:
    print('По итогам жеребьевки первым ходит \033[1mпервый игрок.\033[0m\n   \033[1mИгра началась \033[0m')
    while candies > 0:
        player_one = control_input(control_candies, f'На столе лежит \033[1m{candies}\033[0m конфета. \033[1mХод первого игрока: \033[0m')
        candies -= player_one
        if candies <= 0:
            print('🎉🎉🎉 Победил первый игрок 🎉🎉🎉')
            break
        player_two = control_input(control_candies, f'На столе лежит \033[1m{candies}\033[0m конфета. Ход второго игрока: ')
        candies -= player_two
        if candies <= 0:
            print('🎉🎉🎉 Победил второй игрок 🎉🎉🎉')
            break
else:
    print('По итогам жеребьевки первым ходит \033[1mвторой игрок.\033[0m\n   \033[1mИгра началась \033[0m')
    while candies > 0:
        player_two = control_input(control_candies, f'На столе лежит \033[1m{candies}\033[0m конфета. Ход второго игрока: ')
        candies -= player_two
        if candies <= 0:
            print('🎉🎉🎉 Победил второй игрок 😎')
            break
        player_one = control_input(control_candies, f'На столе лежит \033[1m{candies}\033[0m конфета. \033[1mХод первого игрока: \033[0m')
        candies -= player_one
        if candies <= 0:
            print('🎉🎉🎉 Победил первый игрок 😎')
            break

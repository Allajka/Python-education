# Добавьте игру против бота
# Тут у пользователя нет шансов победить
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
            print('\n🎉🎉🎉 Победил первый игрок 😎')
            break
        computer = candies % (control_candies+1)
        print(f'На столе лежит \033[1m{candies}\033[0m конфета. Компьютер в свой ход забрал \033[1m{computer}\033[0m конфет.')
        candies -= computer
        if candies <= 0:
            print('\nВас обыграл компьютер 😒\nПопробуйте еще!')
            break
else:
    print('Ваш ход будет вторым. \n   \033[1mИгра началась \033[0m')
    while candies > 0:
        computer = candies % (control_candies + 1)
        print(f'На столе лежит \033[1m{candies}\033[0m конфета. Компьютер в свой ход забрал \033[1m{computer}\033[0m конфет.')
        candies -= computer
        if candies <= 0:
            print('\nВас обыграл компьютер 😒\nПопробуйте еще!')
            break
        player = control_input(control_candies, f'На столе лежит \033[1m{candies}\033[0m конфета. \033[1mВаш ход: \033[0m')
        candies -= player
        if candies <= 0:
            print('\n🎉🎉🎉 Вы победили 🎉🎉🎉')
            break

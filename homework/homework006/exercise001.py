# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

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


def print_field(field):
    for row in field:
        for element in row:
            print(element, end=' | ')
        print()


def move(field, search_number, symbol):
    flag = False
    while flag == False:
        for row in field:
            for i in range(len(row)):
                if row[i] == search_number:
                    row[i] = f'\033[1m{symbol}\033[0m'
                    flag = True
        if flag == True:
            break
        else:
            search_number = control_input(size_field,
                                          f'\033[1mПоле занято!\033[0m\nВыберите другую цифру, куда хотите поставить \033[1m{symbol}:\033[0m ')


def victory(field, symbol):
    symbol = f"\033[1m{symbol}\033[0m"
    for i in range(3):
        if field[i][0] == symbol and field[i][1] == symbol and field[i][2] == symbol:
            return True
        if field[0][i] == symbol and field[1][i] == symbol and field[2][i] == symbol:
            return True
    if field[0][0] == symbol and field[1][1] == symbol and field[2][2] == symbol:
        return True
    elif field[0][2] == symbol and field[1][1] == symbol and field[2][0] == symbol:
        return True
    else:
        return False


print('Игра крестики нолики.\nПервый ход делает игрок, ставящий \033[1mкрестики\033[0m.\n')
field = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
size_field = 9
print_field(field)

flag = False
turn = 1
count = 0
while flag == False:
    if turn == 1:
        symbol = "X"
    else:
        symbol = "O"

    player = control_input(size_field, f'Введите цифру, куда хотите поставить \033[1m{symbol}:\033[0m ')
    move(field, player, symbol)
    print_field(field)

    if turn == 1:
        turn = 0
    else:
        turn = 1
    count += 1
    flag = victory(field, symbol)
    if flag:
        print(f'\n🎉🎉🎉 Победил игрок ходивший \033[1m{symbol}\033[0m 🎉🎉🎉')
    if count == 9 and flag == False:
        print('\nИгра закончена ничьей.')
        break

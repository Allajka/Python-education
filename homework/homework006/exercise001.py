# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
field = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def print_field(field):
    for row in field:
        for element in row:
            print(element, end=' | ')
        print()


def fill_num_in_field(field, search_number, symbol):
    for row in field:
        for i in range(len(row)):
            if row[i] == search_number:
                row[i] = f'\033[1m{symbol}\033[0m'


print_field(field)

player_one = int(input('Введите цифру, куда хотите поставить крестик: '))
fill_num_in_field(field, player_one, "O")
print_field(field)

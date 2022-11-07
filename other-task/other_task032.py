# Камень, ножницы, бумага
answer = [input() for i in range(2)]

if answer[0] == 'камень':
    if answer[1] == 'ножницы':
        print("Тимур")
    elif answer[1] == 'бумага':
        print("Руслан")
    else:
        print("ничья")
elif answer[0] == 'ножницы':
    if answer[1] == 'бумага':
        print("Тимур")
    elif answer[1] == 'камень':
        print("Руслан")
    else:
        print("ничья")
elif answer[0] == 'бумага':
    if answer[1] == 'камень':
        print("Тимур")
    elif answer[1] == 'ножницы':
        print("Руслан")
    else:
        print("ничья")

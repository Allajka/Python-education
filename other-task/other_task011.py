# Шахматная доска
# Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())
if col1%2 == 1:
    if row1%2 == 1:
        color1 = "light"
    else: color1 = "dark"
elif col1%2 == 0:
    if row1%2 == 0:
        color1 = "light"
    else: color1 = "dark"

if col2%2 == 1:
    if row2%2 == 1:
        color2 = "light"
    else: color2 = "dark"
elif col2%2 == 0:
    if row2%2 == 0:
        color2 = "light"
    else: color2 = "dark"

if color1 == color2:
    print("YES")
else: print("NO")
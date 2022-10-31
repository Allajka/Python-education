# Валидный номер
# На вход программе подается строка текста. Напишите программу, которая определяет
# является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером если она имеет формат:
# abc-def-hijk или
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

l = input().split("-")
flag = True
for i in l:
    if not i.isdigit():
        flag = False
        break
if len(l) == 4 and flag:
    if l[0] == "7" and len(l[1]) == 3 and len(l[2]) == 3 and len(l[3]) == 4:
        print("YES")
    else:
        print("NO")
elif len(l) == 3 and flag:
    if len(l[0]) == 3 and len(l[1]) == 3 and len(l[2]) == 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


#27 Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел

text = "1 22 53 69 88 8 2"
list_number = (text.split(' '))

max = int(list_number[0])
min = int(list_number[0])
for i in list_number:
    if int(i) > max:
        max = int(i)
    elif int(i) < min:
        min = int(i)
print(max, min)
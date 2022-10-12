# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

with open('file.txt', 'r', encoding='utf-8') as data:
    list_data = data.read().split()

for i in list_data:
    if i == "+":
        index = list_data.index(i)
        del list_data[index]
print(list_data)

new_list = []
k = 5
def sum_number(k, list_data):
    count = 0
    temp = ''
    for i in range(len(list_data)-1):
        if f"x**{k}" in list_data[i]:
            for j in range(len(list_data[i])):
                if list_data[i][j].isdigit():
                    temp += str(list_data[i][j])
                if j > 2:
                    break
            count += int(temp)
            temp = ''
    return count

for i in range(5, 1, -1):
    print(sum_number(i, list_data))


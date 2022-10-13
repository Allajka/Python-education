# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

def sum_number(search, list_data):
    count = 0
    temp = ''
    for i in range(len(list_data) - 1):
        if search in list_data[i]:
            for j in range(len(list_data[i])):
                if list_data[i][j].isdigit():
                    temp += str(list_data[i][j])
                if j > 2:
                    break
            count += int(temp)
            temp = ''
    return count

def delete_row(search, list_data):
    for i in range(len(list_data)):
        if search in list_data[i]:
            del list_data[i]
            return delete_row(search, list_data)
    return list_data

with open('file.txt', 'r', encoding='utf-8') as data:
    list_data = data.read().split()

list_data = delete_row("+", list_data)

new_list = []
k = int(list_data[0][len(list_data[0])-1])

for i in range(k, 1, -1):
    temp = sum_number(f"x^{i}", list_data)
    temp = f"{temp}*x^{i}"
    new_list.append(temp)

list_data = delete_row('*x^', list_data)
temp = sum_number("*x", list_data)
temp = f"{temp}*x"
new_list.append(temp)

list_data = delete_row('*x', list_data)
list_data = delete_row('=', list_data)
list_data = delete_row('0', list_data)
temp = int(list_data[0]) + int(list_data[1])
new_list.append(f"{temp} = 0")

result = " + ".join(new_list)

with open('file.txt', 'a') as data:
    data.write(f'{result}\n')


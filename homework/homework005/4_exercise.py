# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пыталась обойтись без листа, сразу кодировать в строку, но тогда была проблема - как потом восстановить данные если значений больше 10.
def coding_information_list(row):
    coding_list = []
    count = 0
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            count += 1
            if i == len(row) - 2:
                count += 1
                coding_list.append(str(count))
                coding_list.append(row[i])
                count = 0
        else:
            count += 1
            coding_list.append(str(count))
            coding_list.append(row[i])
            count = 0
    return coding_list

def recovery(row):
    decode = ''
    count = ''
    for i in row:
        if i.isdigit():
            count += i
        else:
            decode += i * int(count)
            count = ''
    return decode

string = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwffrtg"
coding_list = coding_information_list(string)
coding_string = ''.join(coding_list)
recovery = recovery(coding_string)

print('RLE алгоритм: модуль сжатия и восстановления данных.\n')
print(f'Исходные данные: {string}')
print(f'Закодированный вариант: {coding_string}')
print(f'Восстановление данных: {recovery}')

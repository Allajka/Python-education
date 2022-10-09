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
                coding_list.append(count)
                coding_list.append(row[i])
                count = 0
        else:
            count += 1
            coding_list.append(count)
            coding_list.append(row[i])
            count = 0
    return coding_list


def coding_information_string(coding_list):
    coding_string = ''
    for i in range(len(coding_list)):
        coding_string = coding_string + str(coding_list[i])
    return coding_string


def data_recovery(coding_list):
    string_recovery = ''
    for i in range(0, len(coding_list), 2):
        string_recovery = string_recovery + (coding_list[i + 1] * coding_list[i])
    return string_recovery


string = "WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
coding_list = coding_information_list(string)
coding_string = coding_information_string(coding_list)
recovery = data_recovery(coding_list)

print('RLE алгоритм: модуль сжатия и восстановления данных.\n')
print(f'Исходные данные: {string}')
print(f'Закодированный вариант: {coding_string}')
print(f'Восстановление данных: {recovery}')

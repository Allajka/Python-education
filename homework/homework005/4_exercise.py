# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def coding_information(row):
    coding = ''
    count = 0
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            count += 1
            if i == len(row) - 2:
                count += 1
                coding += str(count) + row[i]
                count = 0
        else:
            count += 1
            coding += str(count) + row[i]
            count = 0
    return coding

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

user_string = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwffrtg"
coding_string = coding_information(user_string)
recovery = recovery(coding_string)

print('RLE алгоритм: модуль сжатия и восстановления данных.\n')
print(f'Исходные данные: {user_string}')
print(f'Закодированный вариант: {coding_string}')
print(f'Восстановление данных: {recovery}')

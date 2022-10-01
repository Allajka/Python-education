# -*- coding: utf-8 -*-
# Напишите программу, в которой пользователь вводит целое число, а программа меняет каждую цифру на "дополнение до 9"
# 0 - 9, 1 - 8, 2-7 и т.д.

number = 125486  # 874513
control_number = 9
new_number = control_number - number % 10
number = number // 10
tens = 10
temp = 0

while number > 0:
    temp = number % 10
    temp = control_number - temp
    new_number += temp * tens
    tens *= 10
    number = number // 10
print(new_number)

# Перевод чисел из любой системы счисления в десятичную


# def system_calculator(text_number, system_number):
#     result = 0
#     counter = 0
#     for i in range(len(text_number) - 1, -1, -1):
#         result += int(text_number[counter]) * system_number ** i
#         counter += 1
#     return result
#
#
# number = input('Введите число для перевода: ')
# system_number = int(input("Введите цифрой систему счисления: "))
# print(system_calculator(number, system_number))

numbers = int(input())
print(bin(numbers)[2:])
print(oct(numbers)[2:])
print(hex(numbers)[2:].upper())
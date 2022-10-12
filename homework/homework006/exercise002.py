# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
import functions as fun
def control_input(text):
    flag = False
    while flag == False:
        user_number = input(text)
        try:
            user_number = int(user_number)
            if 0 < user_number:
                flag = True
                return int(user_number)
        except ValueError:
            flag == False


print("Программа формирует многочлена в натуральной степень k.")
k = control_input('Введите натуральная степень k: ')
largest = 100
smallest = 0

with open('file.txt', 'w') as data:
    data.write(f'{fun.polynomial(k, largest, smallest)}\n')
    data.write(f'{fun.polynomial(k, largest, smallest)}\n')


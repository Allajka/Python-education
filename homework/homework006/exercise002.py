# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

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


def polynomial(k, largest, smallest):
    result = ''
    for i in range(1, k+2):
        random_number = randint(smallest, largest)
        if i == k+1:
            if random_number == 0:
                result += " = 0"
            else:
                result += f"{random_number} = 0"
        elif i == 1:
            if random_number == 0:
                continue
            elif random_number == 1:
                result += f"x + "
            else:
                result += f"{random_number}*x + "
        else:
            if random_number == 0:
                continue
            else:
                if random_number == 1:
                    result = f"x**{i} + " + result
                else:
                    result = f"{random_number}*x**{i} + " + result
    return result

print("Программа формирует многочлена в натуральной степень k.")
k = control_input('Введите натуральная степень k: ')
largest = 100
smallest = 0
polynomial = polynomial(k, largest, smallest)
print(polynomial)

with open('file.txt', 'w') as data:
    data.write(f'{polynomial}\n')

# Пользователь вводит три числа, а программа определяет может ли существовать треугольник со сторонами, длина которых введена(сумма двух любых треугольников должна быть больше третьего числа)

a = input('Введите сторону A: ')
b = input('Введите сторону B: ')
c = input('Введите сторону C: ')
print('YES' if a + b > c and a + c > b and c + b > a else "NO")

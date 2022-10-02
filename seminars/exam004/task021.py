# Найти корни квадратного уравнения Ax² + Bx + C = 0
# 1) Математикой
# 2) Используя дополнительные библиотеки*
from math import *
a = float(input("a "))
b = float(input("b "))
c = float(input("c "))
x = 0
discriminant = (b ** 2) - (4 * a * c)

if discriminant < 0:
    print("Нет корней")
elif discriminant == 0:
    x = -b / (2 * a)
    print(x)
elif discriminant > 0:
    x1 = (-b - sqrt(discriminant)) / (2 * a)
    x = (-b + sqrt(discriminant)) / (2 * a)
    print(x1)
    print(x)


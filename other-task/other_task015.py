# Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения 
# ax^2 + bx + c = 0.
from math import *

a = -5.64671390542564
b = 7.90460919676605
c = -2.10960556210672

x = 0
discriminant = (b**2) - (4*a*c)

if discriminant < 0:
    print("Нет корней")
elif discriminant == 0:
    x = -b/(2*a)
    print(x)
elif discriminant > 0:
    x1 = (-b - sqrt(discriminant))/(2*a)
    x = (-b + sqrt(discriminant))/(2*a)
    if x1<x:
        print(x1)
        print(x)
    else:
        print(x)
        print(x1)

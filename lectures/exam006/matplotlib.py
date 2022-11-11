import matplotlib.pyplot as plt
import random

fun = lambda x: random.randint(1, 10)
points = list(map(fun, range(1, 10)))
print(points)
p = plt.plot(points, 'r>')
# маркер - 'ro' - первое значение цвет, второе фигура
# r - red, b - blue, y - yellow и т.д.
#  ., , , o, v, ^, <	, >, 1, 2, 3, 4, 8, s, p, P, *, h, H, +, x, X, D, d, |, _,

x = list(map(fun, range(1, 10)))
y = list(map(fun, range(1, 10)))
print(x)
print(y)
plt.plot(x, y, 'y-')
plt.show()

x = list(range(1, 200))
fx = [i * i for i in x]

# Заливка фона
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes

plt.axes(facecolor='white')
plt.plot(x, fx)
plt.show()

# Настройки
# https://matplotlib.org/stable/tutorials/introductory/customizing.html

import matplotlib.pyplot as plt
import matplotlib as mpl

x = list(range(-200, 200))
fx = [i ** 2 + 2 * i - 3 for i in x]

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes

mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['lines.linestyle'] = '-.'  # '--' меняем вид линии
mpl.rcParams['lines.color'] = 'C0'

plt.axes(facecolor='white')
plt.plot(x, fx)
plt.show()

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

x = list(range(0, 500, 2))
y = list(map(lambda a: sqrt(a), x))

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()

#  Наименование осей
ax.set_xlabel('x')
ax.set_ylabel('sqrt(x)')

plt.show()

# треугольник
import matplotlib.pyplot as plt
import random

# random.randint(1, 10)

vx = [1.0, 2.0, 3.0]
vy = [1.0, 2.0, 1.0]

sx = vx[0]
sy = vy[0]

px = []
py = []

for i in range(1, 1000):
    r = random.randint(0, 2)
    sx = (sx + vx[r]) / 2
    sy = (sy + vy[r]) / 2
    px.append(sx)
    py.append(sy)

plt.plot(px, py, 'o')
plt.show()

# более детальный треугольник
import random
import matplotlib.pyplot as plt

x = [1.0, 2.0, 3.0]
y = [1.0, 2.0, 1.0]

sx = x[0]
sy = y[0]

px = []
py = []

for i in range(1, 100000):
    r = random.randint(0, 2)
    sx = (sx + x[r]) / 2
    sy = (sy + y[r]) / 2
    px.append(sx)
    py.append(sy)

fig, ax = plt.subplots()

# маркеры цветов 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w' , RGB: #00ff00
ax.scatter(px, py, c='red', s=1)
ax.set_facecolor('black')

# ax.grid()
# ax.set_xlabel('')
# ax.set_ylabel('')
fig.set_figwidth(15)  # размеры
fig.set_figheight(10)  # размеры
plt.show()

# кубик

import random
import matplotlib.pyplot as plt

count = 10000  # кол-во бросков
x = list(range(1, 7))
y = [0 for i in x]  # список из 6 нулей, отвечающий за выпадения значений кубика

fig, ax = plt.subplots()

for _ in range(count):
    y[random.randint(0, 5)] += 1

ax.bar(x, y)
#
y.sort()
# print('{}%'.format(round((y[5] - y[0]) / count * 100, 3)))
stat = [f'{i + 1}: {round(y[i] / count * 100)}%' for i in range(0, 6)]
print(stat)
plt.show()



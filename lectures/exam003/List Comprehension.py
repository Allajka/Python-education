# List Comprehension
# Общий вид - создание списка и наполнение числами в квадрате от 0 до 9
squares = []
for x in range(10):
    squares.append(x ** 2)
# print - [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Упрощенный вид наполнения списка
squares = [x ** 2 for x in range(10)]
#  print - [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# С условиями список
odds = [x for x in range(10) if x % 2 != 0]
# print - [1, 3, 5, 7, 9]

# С условиями кортеж
odds = [(x, x ** 2) for x in range(10) if x % 2 != 0]
# print - [(1, 1), (3, 9), (5, 25), (7, 49), (9, 81)]

# если в условии нужен else, то всё условие пишется до for
odds = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
# print - [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]

# Обработка полученных значений через функцию
f = lambda x: x + 10
odds = [(x, f(x)) for x in range(10) if x % 2 != 0]
print(odds)
# Пример генерации списка с вложенным for
first = []

for x in range(1, 5):
    for y in range(5, 1, -1):
        if x != y:
            first.append((x, y))

second = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]

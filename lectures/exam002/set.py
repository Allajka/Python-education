# Множества
a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = {'a': 2, 'b': 3}
print(type(a))  # set
print(type(b))  # set
print(type(c))  # dict

colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red')  # добавления элемента который есть, не добавиться
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red')  # удаление
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' - удаляя так будет ошибка
colors.discard('red')  # но удаляя таким способом ошибки не будет
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { } - очистить
print(colors)  # set()

a = {1, 2, 3, 5, 8}
print(a)
b = {2, 5, 8, 13, 21}
print(b)
c = a.copy()  # c = {1, 2, 3, 5, 8} - множество на основе имеющегося
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}  - объединение множеств(без повторений)
i = a.intersection(b)  # i = {8, 2, 5} - пересечение(одинаковые)
dl = a.difference(b)  # dl = {1, 3} - разность(отличия)
dr = b.difference(a)  # dr = {13, 21} - разность(отличия)
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}
print(q) # dr = {13, 21} - разность сразу двух множеств

s = frozenset(a)  # замороженное, неизменяемое множество

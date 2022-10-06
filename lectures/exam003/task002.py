# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

def select(f, col): #но лучше использовать функцию map
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
print(data)

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)
print(res)
print()
res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

numbers = [i for i in range(10)]
res = list(filter(lambda x: not x%2, numbers))
print(res)

user = ['user1', 'user2', 'user3', 'user4']
ids = [4, 5, 6, 7]
total = list(zip(user, ids)) # [('user1', 4), ('user2', 5), ('user3', 6), ('user4', 7)]
print(total)

user = ['user1', 'user2', 'user3', 'user4']
total2 = list(enumerate(user)) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4')]
print(total2)
import functions as f

print(f.f(1))
print(f.concatenatio('a', 's', 'd', 'w'))  # asdw
print(f.concatenatio('a', '1', 'd', '2'))  # a1d2

list = []
for e in range(1, 10):
    list.append(f.fib(e))
print(list)  # 1 1 2 3 5 8 13 21 34

# Кортежи
a = (2, 33, 6, 9)
print(a)
print(a[2])
for i in a:
    print(i, end=' ')

t = tuple(['red', 'green', 'blue'])
red, green, blue = t  # распаковка кортежа в отдельные переменные
print('r:{} g:{} b:{}'.format(red, green, blue))

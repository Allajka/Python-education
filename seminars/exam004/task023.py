# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('N = '))
d = {}
for i in range(1, n+1):
    d.update({i: 3*i + 1}) # и ключ и значение
print(d)

n = int(input('N = '))
d = {}
for i in range(1, n+1):
    d.setdefault(i, 3*i + 1) # если не добавить значение добавиться ключ и может значение
print(d)


n = int(input('N = '))
d = {}
for i in range(1, n+1):
    d[i] = 3*i + 1
print(d)

# дип каприкеншен
number = int(input('Input the number: '))
d = {i : 3*i + 1 for i in range(1,number+1)}

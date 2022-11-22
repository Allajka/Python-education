n, l = int(input()), []

for _ in range(n):
    l.append([int(i) for i in input().split()])

up, bottom, right, left = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            up += l[i][j]
        if i > j and i > n - 1 - j:
            bottom += l[i][j]
        if i > j and i < n - 1 - j:
            left += l[i][j]
        if i < j and i > n - 1 - j:
            right += l[i][j]

print(f'Верхняя четверть: {up}')
print(f'Правая четверть: {right}')
print(f'Нижняя четверть: {bottom}')
print(f'Левая четверть: {left}')


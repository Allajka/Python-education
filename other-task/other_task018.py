# Решите уравнение в натуральных числах 28n + 30 k + 31 m = 36528n+30k+31m=365.
total = 0
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            if 28 * x + 30 * y + 31 * z == 365:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print()
# 12x+13y=777.
# предел 777 // 12 = 64
# предел 777 // 11 = 59
total = 0
for x in range(1, 65):
    for y in range(1, 60):
        if 12 * x + 13 * y == 777:
            total += 1
            print('x =', x, 'y =', y)
print('Общее количество натуральных решений =', total)

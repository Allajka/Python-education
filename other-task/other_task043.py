# Максимальный в области

n, l = int(input()), []

for _ in range(n):
    l.append([int(i) for i in input().split()])

maximum = l[0][0]

for i in range(n):
    for j in range(n):
        if i >= j and i <= n - 1 - j:
            if l[i][j] > maximum:
                maximum = l[i][j]


for i in range(n):
    for j in range(n):
        if i <= j and i >= n - 1 - j:
            if l[i][j] > maximum:
                maximum = l[i][j]
print(maximum)

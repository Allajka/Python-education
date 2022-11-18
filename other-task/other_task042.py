# След матрицы

n, res, l = int(input()), 0, []

for _ in range(n):
    l.append([int(i) for i in input().split()])

for i in range(n):
    res += l[i][i]

print(res)
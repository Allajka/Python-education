row, col = int(input()), int(input())

l = [[int(i) for i in input().split()] for _ in range(row)]

maximum, index_row, index_col = l[0][0], 0, 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] > maximum:
            maximum, index_row, index_col = l[i][j], i, j

print(index_row, index_col)

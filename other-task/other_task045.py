def print_matrix(matrix, width=1):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j]).ljust(width), end=' ')
        print()


row, col = 4, 6

matrix = [[0] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        matrix[i][j] = i * j

print_matrix(matrix, width=3)

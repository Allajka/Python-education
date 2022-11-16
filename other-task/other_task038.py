# Треугольник Паскаля

def pascal(start_list, end):
    for row in range(end + 1):
        temp = []
        for i in range(len(start_list[row]) - 1):
            res = start_list[row][i] + start_list[row][i + 1]
            temp.append(res)
            res = 0
        temp.append(1)
        temp.insert(0, 1)
        start_list.append(temp)
    return start_list[end]


start_list = [[1]]
end = int(input())

print(pascal(start_list, end))

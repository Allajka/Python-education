# Координатные четверти

def coordinates(x,y):
    if x >= 0 and y >= 0:
        return 1
    elif x <= 0 and y >= 0:
        return 2
    elif x <= 0 and y <= 0:
        return 3
    elif x >= 0 and y <= 0:
        return 4

count1, count2, count3, count4 = 0, 0, 0, 0

for _ in range(int(input())):
    dot = input().split()
    quarter = coordinates(int(dot[0]),int(dot[1]))
    if quarter == 1:
        count1 +=1
    elif quarter == 2:
        count2 +=1
    elif quarter == 3:
        count3 +=1
    elif quarter == 4:
        count4 += 1

print(f"Первая четверть: {count1}\nВторая четверть: {count2}\nТретья четверть: {count3}\nЧетвертая четверть: {count4}")
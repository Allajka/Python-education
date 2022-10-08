# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = "WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
repetition = []
count = 0

for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count +=1
        if i == len(text)-2:
            count += 1
            repetition.append(count)
            repetition.append(text[i])
            count = 0
    else:
        count += 1
        repetition.append(count)
        repetition.append(text[i])
        count = 0

print(repetition)




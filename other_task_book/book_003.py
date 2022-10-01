# Фибоначчи

end = int(input("Введите размер списка чисел Фибоначчи: "))
list_number = [1, 1]
for i in range(0, end):
    list_number.append(list_number[i] + list_number[i+1])
print(list_number)

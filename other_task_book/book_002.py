# Напишите программу, создающую список из чисел которые при делении на 5 дают в остатке 3. Отобразите список в прямом и обратном порядке.
# end = int(input("До какого числа создавать список: "))
# list_number = []

# for i in range(1, end):
#     if i % 5 == 3:
#         list_number.append(i)

# print(list_number)
# print(list(reversed(list_number)))

# по формуле 5k+3, где k = 0,1,2,3
end = int(input("Введите размер спика: "))
list_number = [5*i+3 for i in range(0, end)]
print(list_number)
print(list(reversed(list_number)))
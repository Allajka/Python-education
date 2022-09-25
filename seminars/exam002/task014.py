#5  Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

n = int(input("Введите целое положительное число: "))
temp = n
size = 0
while(temp > 0):
    temp //= 10
    size += 1
temp = n
numbers = []

for i in range(size):
    numbers.append(temp%10) 
    temp = temp//10

maximum = numbers[0]
index = 1
while(index < len(numbers)):
    if maximum < numbers[index]:
        maximum =numbers[index]
    index += 1

print(f"MAX = {maximum}")

# a = int(input("Введите число: "))
# maxNumber = 0
# while a > 0:
#     b = a % 10
#     if b > maxNumber:
#         maxNumber = b
#         if maxNumber == 9:
#             break
#     a //= 10

# print(maxNumber)

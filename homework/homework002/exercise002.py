# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Factorial(number):
    if number == 1:
        return 1
    else: return number * Factorial(number - 1)

print("Программа выдает набор произведений чисел от 1 до N.")
number = int(input("Введите число N: "))
list_number = []
for i in range(1, number+1):
    list_number.append(Factorial(i))
print(list_number)


# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

n = int(input("Введите число: "))
temp, total_sum, size, total_multip = n, 0, 0, 1

while temp>0:
    total_sum += temp%10
    size += 1
    total_multip *= temp%10
    temp //=10
middle = total_sum/size
first = n//(10**(size-1))
last_sum = first+(n%10)
print(f"Сумма цифр {total_sum}")
print(f"Количество цифр {size}")
print(f"Произведение цифр {total_multip}")
print(f"Среднее арифметическое {middle}")
print(f"Первая цифра {first}")
print(f"Сумма первой и последней цифры {last_sum}")

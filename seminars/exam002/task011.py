#2 Сформировать список из  N членов последовательности. 
#Для N = 5: 1, -3, 9, -27, 81 и т.д.
# https://docs.google.com/document/d/1UngwpzzA0buLowV3Sw0luH172b03XFoh37uccRz3x_8/edit#heading=h.m7evrbvl3c8a

n = int(input("Введите число N: "))
list = []
for i in range(n):
    list.append((-3)**i) 
print(list)

start = 1
for i in range(1, n+1):
    print(start, end=' ')
    start *= -3

print()
list = [(-3)**i for i in range(n)]
print(f"Итоговая последовательность: {list}")
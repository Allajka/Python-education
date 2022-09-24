#На числовой прямой даны два отрезка: [a1; b1] [a2;b2]. Напишите программу, которая находит их пересечение.
# Пересечением двух отрезков может быть:
# отрезок;
# точка;
# пустое множество.
# Гарантируется, что a1<b1 и  a2<b2

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if b1<a2 or a1>b2:
    print("пустое множество")
elif b1 == a2:
    print(a2)
elif a1 == b2:
    print(a1)
elif a1 <= a2 < b1:
    if a1 < a2 < b2 and b1>b2:
        print(a2, b2)
    else: print(a2, b1)
elif a1< b1 < b2:
    print(a1, b1)
elif (a2<a1<b2)or (a1>a2 and b1<=b2):
    print( a1, b2)
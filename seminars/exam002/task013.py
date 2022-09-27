#4  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
# Считаем 3 + 33 + 333 = 369.

# n = int(input("Введите число n: "))
# print(f"{n} + {n*10+n} + {(n*10+n)*10 +n} = {n + (n*10+n) + ((n*10+n)*10 +n)}")

n = input("Введите число n: ")
print(int(n) + int(n+n) + int(n+n+n))

# n = int(input('Введите число: '))
# interim = n
# l = 1
# while interim // 10 > 0:
#     interim = interim // 10
#     l += 1

# d = int(input('Введите количество слагаемых: '))
# result = 0
# i = 0
# for i in range(d):
#     result = result + n*(d-i)*10*(i*l)
#     i += 1
# print(result)
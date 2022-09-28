#4  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
# Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число n: "))
# print(f"{n} + {n*10+n} + {(n*10+n)*10 +n} = {n + (n*10+n) + ((n*10+n)*10 +n)}")

# print(int(n) + int(n+n) + int(n+n+n))

result = 0
for i in range(1, n):
    temp = eval(str(n)*i) 
    result += temp
    print(f"{str(n)*i} + ", end='')
else:
    temp = eval(str(n)*(i+1)) 
    result += temp
    print(f"{str(n)*(i+1)} ", end='')
print(f"= {result}")
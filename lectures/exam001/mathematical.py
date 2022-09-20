a = 8
b = 3

print(a + b)
print(a ** b)
print(a // b)
print(a % b)
print(a / b)
print(round(a / b,3))
print(int(a / b))

a, b, c = 1, 2, 3
# a: 1 b: 2 c: 3
print('a: {} b: {} c: {}'.format(a, b, c))

print(c > b and b > a) #True
print(a > b or a != c) #True

f = [1, 2, 3, 4]
print(2 in f) # 2 присутствует в списке f
print(not 2 in f) # 2 НЕ присутствует в списке f

even = f[0] % 2 == 0 # проверка на четность
print(even)
even = not f[0] % 2 # проверка на четность
print(even)
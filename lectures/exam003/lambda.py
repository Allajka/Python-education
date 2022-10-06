# lambda

def sum(x, y):
    return x + y

s = sum  # переменная хранит целиком функцию
print(s(2, 3))  # можем вызвать эту переменную как функцию
# но можем записать все это проще

s1 = lambda q, w: q+w
print(s1(2,7))

def mylt(x, y):
    return x * y


def calc(op, x, y):  # в качестве аргумента целая функция
    print(op(x, y))
    #return op(x, y)


calc(sum, 2, 5)  # передаем в нашу функцию - функцию и переменные
calc(mylt, 2, 5)
calc(s, 2, 5) # передаем в нашу функцию - лямду и переменные
print()
calc((lambda x, y: x+y), 7, 2)
calc((lambda x, y: x*y), 7, 2)
calc((lambda x, y: x/y), 7, 2)

def a(x):
    return x**2


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
# Передача неограниченного кол-ва аргументов - через указание *
def concatenatio(*params):
    res: str = ""  # явно указываю с каким типом хочу работать
    for item in params:
        res += item
    return res

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

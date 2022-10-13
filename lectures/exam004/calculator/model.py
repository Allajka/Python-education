x = 0
y = 0


def init(a, b):  # инициализация значений двух переменных
    global x  # связываем переменную мне метода
    global y
    x, y = a, b


def amount(sign):  # логика, действия над данными
    return eval(f"{x} {sign} {y}")

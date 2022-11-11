# Предикат делимости
def func(num1, num2):
    return num1 % num2 == 0


print("делится") if func(int(input()), int(input())) else print("не делится")


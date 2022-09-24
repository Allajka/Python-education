#Найти расстояние между двумя точками пространства
x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

print(round(distance,2))

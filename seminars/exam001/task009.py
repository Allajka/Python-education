# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

q = int(input("Введите номер четверти: "))

if q == 1:
    print("Допустимые значения координат для точек этой четверти: x > 0 и y > 0")

if q == 2:
    print("Допустимые значения координат для точек этой четверти: x < 0 и y > 0")

if q == 3:
    print("Допустимые значения координат для точек этой четверти: x < 0 и y < 0")
    
if q == 4:
    print("Допустимые значения координат для точек этой четверти: x > 0 и y < 0")

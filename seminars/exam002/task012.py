#3 Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time = int(input("Введите секунды: "))

hours = time//3600
minutes = (time % 3600)//60
# seconds = time-(hours * 3600) - minutes * 60
seconds = time % 60
print(f'{hours}:{minutes}:{seconds}')
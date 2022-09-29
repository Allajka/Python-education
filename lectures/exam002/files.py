# Добавление в файл вариант 1
colors = ["red", "green", "белый"]
# data = open('file.txt', 'a')  # создаем переменную и связываем ее с текстовым файлом а - дозапись в файл
data = open('file.txt', 'w')  # создаем переменную и связываем ее с текстовым файлом w - перезапись данных в файле
# data.writelines(colors) # разделителей не будет
data.write(colors[0])  # Только str
data.write('\nLENE 2\n')
data.write('LENE 3\n')
data.close()  # закрыть файл, разорвать подключение.

# Добавление в файл вариант 2
with open('file.txt', 'a') as data:
    data.write('LENE 12\n')
    data.write('LENE 13\n')  # разрыв связи происходит автоматически

# Чтение файла
path = 'file.txt'  # путь к папке
data = open(path, 'r')  # откроем в режиме чтения
for line in data:
    print(line, end='')
data.close()

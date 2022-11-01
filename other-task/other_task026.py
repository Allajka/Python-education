# объявление функции
def convert_to_python_case(text):
    for i in range(1, len(txt)):
        if txt[i].isupper():
            txt = txt[:i] + "_" + txt[i].lower() + txt[i + 1:]
    return txt.lower()

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

txt = 'ThisIsCamelCased'


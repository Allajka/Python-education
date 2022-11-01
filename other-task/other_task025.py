# объявление функции
def is_correct_bracket(text):
    for i in range(len(text) // 2):
        text = text.replace("()", "")
    if text == "":
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))



txt = ')(())('


print(txt)
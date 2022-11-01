# объявление функции
def is_pangram(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alphabet:
        if i not in text.lower():
            return False
    return True
# считываем данные
text = 'The jay pig fox zebra and my wolves quack'

# вызываем функцию
print(is_pangram(text))



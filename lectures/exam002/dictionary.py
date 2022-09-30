dictionary = {}
dictionary = \
    {
        'up': '|',
        'left': '>',
        'down': '<',
        'right': '|'
    }
# типы ключей могут отличаться
print(dictionary)
print(dictionary['left'])
# пройтись по всем ключам
for k in dictionary.keys():
    print(k)
# пройтись по всем значениям
for k in dictionary.values():
    print(k)

for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))
print(type(dictionary))
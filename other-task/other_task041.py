# Подсписки списка
text = [[]]
data = "a b c d e f".split()
text += [[i] for i in data]

counter = 1
for control in range(1, len(data)):
    for i in range(len(data) - control):
        res = text[counter] + [data[i + control]]
        counter += 1
        text.append(res)
    counter += 1
print(text)


# Разбиение на чанки

text = "a b c d e f r g b".split()
n = 2
l = []
for i in range(0, len(text), n):
    temp = []
    for j in range(i, i + n):
        if j <= len(text) -1:
            temp += text[j]
    l.append(temp)
print(l)

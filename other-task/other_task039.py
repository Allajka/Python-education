# Упаковка дубликатов

text = "w w w o r l d g g g g r e a t t e c c h e m g g p w w".split()

l = [[text[0]]]

for i in range(1, len(text)):
    if not text[i] == text[i-1]:
        l.append([text[i]])
    else:
        l[-1].append(text[i])

print(l)
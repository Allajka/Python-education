# Кремниевая долина
text = [input() for i in range(int(input()))]
search = "anton"

for i in range(len(text)):
    temp = ""
    words = ''
    for j in range(len(text[i])):
        if text[i][j] in search:
            temp += text[i][j]
    text[i] = temp
    if len(text[i]) > 0:
        count = 0
        temp = search[count]

        for k in range(len(text[i])):
            if text[i][k] == temp:
                words += temp
                count += 1
                if count == len(search):
                    break
                temp = search[count]
        text[i] = words
    if words == search:
        print(i + 1, end=' ')
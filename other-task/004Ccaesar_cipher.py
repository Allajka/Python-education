# eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# symbol = [" ", ",", ".", "!", "?"]
#
# print("Выберите язык: aнгл=e, рус=r")
# lan = input()
# print("Выберите шифрование: шифрование - ch, дешифрование - def")
# chif = input()
# print("Введите ключ шифрования")
# n = int(input())
# print("Введите фразу")
# f = input()
#
#
# def chru(chifr, n, l, fraza):
#     if l == 'r':
#         moch = 32
#     if l == 'e':
#         moch = 26
#     if chifr == 'def':
#         n = -n
#     for i in range(len(fraza)):
#         if fraza[i].isalpha():
#             if fraza[i] == fraza[i].upper():
#                 for j in range(moch):
#                     if moch == 32:
#                         if fraza[i] == rus_upper_alphabet[j]:
#                             print(rus_upper_alphabet[(j + n) % moch], end='')
#                             break
#                     if moch == 26:
#                         if fraza[i] == eng_upper_alphabet[j]:
#                             print(eng_upper_alphabet[(j + n) % moch], end='')
#                             break
#             elif fraza[i] == fraza[i].lower():
#                 for j in range(moch):
#                     if moch == 32:
#                         if fraza[i] == rus_lower_alphabet[j]:
#                             print(rus_lower_alphabet[(j + n) % moch], end='')
#                             break
#                     if moch == 26:
#                         if fraza[i] == eng_lower_alphabet[j]:
#                             print(eng_lower_alphabet[(j + n) % moch], end='')
#                             break
#         else:
#             print(fraza[i], end='')
#
#
# chru(chif, n, lan, f)
#

def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()

text = input().split()
for i in range(len(text)):
    count = 0
    for j in text[i]:
        if j.isalpha():
            count +=1
    chipher = ""
    for j in range(len(text[i])):
        if text[i][j].isalpha():
            chipher += sdvig(text[i][j], count)
        else:
            chipher += text[i][j]
    text[i] = chipher

print(*text)

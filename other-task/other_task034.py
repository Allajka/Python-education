# Орел и решка
# counter = 0
# maxi = 0
# text = input()
# for i in range(len(text)):
#     if text[i] == "Р":
#         counter += 1
#         if i == len(text) -1:
#             maxi = counter
#     elif text[i] == 'О':
#         if counter > maxi:
#             maxi = counter
#         counter = 0
# print(maxi)
text = input().split("О")
print(len(max(text)))
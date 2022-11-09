# Роскомнадзор запретил букву а

def delte_letter(text, index_del):
    return text[:index_del] + text[index_del+1:]

alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

answer = input() + " запретил букву"
#
# flag = False
# for i in range(len(alphabet)):
#     if alphabet[i] in answer:
#         print(answer + " " + alphabet[i])
#         flag = True
#     if answer == alphabet[i] * len(answer):
#         break
#     if flag:
#         amount_letter = answer.count(alphabet[i])
#         for _ in range(amount_letter):
#             index_text = answer.find(alphabet[i])
#             answer = delte_letter(answer, index_text).strip()
#         if "  " in answer:
#             answer = answer.replace("  ", " ")
#         flag = False

for letter in alphabet:
    if letter in answer:
        print(answer, letter)
        answer = answer.replace(letter, "").replace('  ', ' ').strip()


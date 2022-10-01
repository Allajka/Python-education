# Реализовать алгоритм перемешивания списка.
number = [1, 2, 8, 6, 5, 7, 12, 55]
print(number)
# for i in range(0, int(len(number)//2)):
#     number[i], number[len(number)-i - 1] = number[len(number)-i - 1], number[i]
#
#
# print(number)
print(number[::-1])

# Реализовать алгоритм перемешивания списка.
# from time import time
# import time
# original = [0, 2, 4, 6, 9]
# print(original)
#
# def time_random():
#     return time() - float(str(time()).split('.')[0])
#
# def random_number(min, max):
#     return int(time_random() * (max - min) + min)
#
# def mixing_list(array):
#     for i in range(0, len(array)):
#         rnd_position = int(random_number(0, len(array)))
#         temp1 = original[i]
#         original[i] = original[rnd_position]
#         original[rnd_position] = temp1
#
# mixing_list(original)
# print(original)


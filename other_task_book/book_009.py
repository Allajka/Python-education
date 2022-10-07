# Напишите программу в которой сравниваются (на предмет равенства) два числовых списка.
# Два списка равны, если они одинакового размера и у них совпадают соответствующие элементы.

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = [2, 2, 3, 4, 5]


def compare_list(first_list, second_list):
    if len(first_list) == len(second_list):
        for i in range(len(first_list)):
            if not first_list[i] == second_list[i]:
                return False
            else:
                return True
    else:
        return True


print("Равны" if compare_list(a, b) else "Не равны")
print("Равны" if compare_list(a, c) else "Не равны")

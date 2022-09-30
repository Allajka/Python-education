# ���������
a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = {'a': 2, 'b': 3}
print(type(a))  # set
print(type(b))  # set
print(type(c))  # dict

colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red')  # ���������� �������� ������� ����, �� ����������
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red')  # ��������
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' - ������ ��� ����� ������
colors.discard('red')  # �� ������ ����� �������� ������ �� �����
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { } - ��������
print(colors)  # set()

a = {1, 2, 3, 5, 8}
print(a)
b = {2, 5, 8, 13, 21}
print(b)
c = a.copy()  # c = {1, 2, 3, 5, 8} - ��������� �� ������ ����������
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}  - ����������� ��������(��� ����������)
i = a.intersection(b)  # i = {8, 2, 5} - �����������(����������)
dl = a.difference(b)  # dl = {1, 3} - ��������(�������)
dr = b.difference(a)  # dr = {13, 21} - ��������(�������)
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}
print(q) # dr = {13, 21} - �������� ����� ���� ��������

s = frozenset(a)  # ������������, ������������ ���������

#Google search - 2
#На вход программе подается натуральное число n, затем n строк, затем число
# k — количество поисковых запросов, затем kk строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

l = []
for i in range(int(input())):
    l.append(input())

s = []
for i in range(int(input())):
    s.append(input())

counter = 0

res = []
for row in l:
    for search in s:
        if search.lower() in row.lower():
            counter += 1
        if counter == len(s):
            res.append(row)
    counter = 0


print(*res, sep='\n')
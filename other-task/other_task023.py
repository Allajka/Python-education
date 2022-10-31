# Алфавит
start = 97
end = start +26
count = 1
l = []
for i in range(start, end):
    l.append(chr(i) * count)
    count += 1
print(l)
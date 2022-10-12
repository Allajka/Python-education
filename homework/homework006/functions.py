from random import randint
def polynomial(k, largest, smallest):
    l = [str((randint(smallest, largest))) for i in range(k+1)]

    for i in range(k+1):
        if int(l[i]) == 0:
            if i == k:
                l[i] = " = 0"
            else:
                continue
        elif i == k-1:
            l[i] += f"*x"
        elif i == k:
            l[i] += " = 0"
        elif int(l[i]) == 1:
            l[i] = f"x**{k-i}"
        else:
            l[i] += f"*x**{k-i}"

    for i in l:
        if i == "0":
            index = l.index(i)
            del l[index]

    result = " + ".join(l)
    return result
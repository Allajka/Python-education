# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(f"not {x} v {y} v {z} = not {x} ^ not {y} ^ not {z} True")
            else:
                print(f"not {x} v {y} v {z} = not {x} ^ not {y} ^ not {z} False")

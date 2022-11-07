# Произведение чисел
n = [int(input()) for _ in range(int(input()))]
result = int(input())
count = 0
answer = []
# answer = [n[i]*n[j] for i in range(len(n)) for j in range(1, i+1) if not j == 5 and i != j]
for i in range(len(n)):
    for j in range(i + 1):
        if not j == 5 and i != j:
            answer.append(n[i] * n[j])

if result in answer:
    count += 1
print("ДА") if count > 0 else print("НЕТ")

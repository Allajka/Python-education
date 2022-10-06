numbers = [i for i in range(1, 20)]
print(numbers)
numbers = list(map(lambda x: x + 10, numbers))
print(numbers)

# преобразование вводимой строки чисел через пробел, в список цифр
user_numbers = list(map(int, input().split()))
print(user_numbers)
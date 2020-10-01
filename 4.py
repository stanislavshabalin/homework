number = int(input("Введите ваше число: "))

max_digit = 0
while number > 0:
    next_digit, number = number % 10, number // 10
    max_digit = max(next_digit, max_digit)


print(max_digit)

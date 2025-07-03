def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
number = 2148348
print("Sum of digits of", number, "is:", sum_of_digits(number))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example
print("Factorial of 5:", factorial(5))

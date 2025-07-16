def fibonacci(n, a=1, b=2):
    if n == 0:
        return
    print(a, end=' ')
    fibonacci(n - 1, b, a + b)

# Example
print("Fibonacci Terms:")
fibonacci(7)

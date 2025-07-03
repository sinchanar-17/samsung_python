def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

# Print first N Fibonacci numbers
def print_fibonacci_series(N):
    for i in range(N):
        print(fibo(i), end=' ')

# Example usage
print("Fibonacci Series:")
print_fibonacci_series(10)

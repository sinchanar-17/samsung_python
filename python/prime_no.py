#Print the Prime numbers in decreasing order between m and n (m < n)
m = int(input("Enter the ending range : "))
n = int(input("Enter the starting range: "))

if n >= m:
    print("Invalid input. Make sure m is greater than n.")
else:
    print(f"\nPrime numbers between {n} and {m} in decreasing order:")

    for num in range(m, n - 1, -1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
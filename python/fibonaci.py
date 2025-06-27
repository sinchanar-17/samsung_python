#Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2
nth_term = int(input("Enter the term you want to find: "))
a, b = 0, 1
for i in range(2, nth_term + 1):
    c = a + b
    a = b
    b = c
print("The Fibonacci term at", nth_term, "is", b)

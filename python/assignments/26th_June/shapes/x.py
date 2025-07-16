#program to print x shape
def x_shape(n):
    if n < 1:
        return 'invalid size'
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1:
                print('* ', end = "")
            else:
                print('  ', end = "")
        print()
n = int(input("enter size of x shape: "))
x_shape(n)
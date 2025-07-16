#program that prints x inside a hollow square
def x_inside_hollow_square(n):
    if n <= 3:
        return 'invalid input, enter a larger size'
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i +j == n - 1:
                print('*', end=' ')
            else:
                print(" ", end=' ')
        print()
n = int(input("enter size of square:"))
print(x_inside_hollow_square(n))
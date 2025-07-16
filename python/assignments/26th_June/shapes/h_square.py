# program to print a hollow square of given size
def hollow_square(n):
    if n <= 0:
        return "Invalid input"
    for i in range(n):
        if  i == 0 or i == n - 1:
            print("* " * n)
        else:
            print('* ' + ' ' * (n+1) + '*')
n = int(input("enter size of square: "))
hollow_square(n)
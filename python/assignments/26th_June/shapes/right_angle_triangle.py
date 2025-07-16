# code to print a right angled triangle
def right_triangle(n):
    if n<=1:
        print('invalid input, enter a number greater than 1')
    else:
        for i in range(1, n+1):
            print ('* ' * i)
n = int(input("enter number of lines:"))
right_triangle(n)
        
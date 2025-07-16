# To print Equilateral Triangle

number_of_lines = int(input("Enter the number of lines you want the right-angle triangle to be: "))


for i in range(1, number_of_lines + 1):
    print(" " * (number_of_lines - i) + "* " * i)
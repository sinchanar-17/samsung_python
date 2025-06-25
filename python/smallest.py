#find smallest of 3 distinct numbers

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
num3 = int(input("Enter a number"))
if num1 != num2 != num3:
    if num1 < num2 and num1 < num3:
        print(num1,"is the smallest")
    elif num2 < num1 and num2 < num3:
        print(num2,"is the smallest")
    else:
        print(num3,"is the smallest")
else:
    print("Enter 3 different numbers")
number = int(input("Enter the number"))
biggest_digit = number%10
for digit in str(number):
    if int(digit)>=biggest_digit:
        biggest_digit=int(digit)
print("The biggest digit is ",biggest_digit)
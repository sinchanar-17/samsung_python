#Count number of Prime digits in a number
number = input("Enter a number: ")
count = 0

for digit in number:
    if digit in ['2', '3', '5', '7']:
        count += 1

print("The total number of prime digits is:", count)
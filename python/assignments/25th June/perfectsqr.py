#check if a +ve integer is perfect square

number = int(input("Enter a positive integer: "))

i = 1
while i * i <= number:
    if i * i == number:
        print(number, "is a perfect square")
        break
    i += 1


#**4. Given a number, find very next possible bigger number that has all the digits of the given number.
num = input("Enter a number: ")
digits = list(num)

i = len(digits) - 2
while i >= 0 and digits[i] >= digits[i + 1]:
    i -= 1

if i == -1:
    print("No greater number possible")
else:
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    right_part = digits[i + 1:]
    right_part.sort()
    digits = digits[:i + 1] + right_part
    print("Next bigger number:", ''.join(digits))
# Accpet a number from the user (4 digit number where a digit can repeat at most 2 times )and print the coutn of recursions reqired to arrive at Karpekar's Constant.
# Karpekar's Constant is 6174
def karpekar_constant(n):
    count = 0
    while n != 6174:
        digits = []
        for ch in str(n): 
            digits.append(ch)
        asc = sorted(digits)
        asc_num = ""
        for ch in asc:
            asc_num += ch
        desc = sorted(digits, reverse=True)
        desc_num = ""
        for ch in desc:
            desc_num += ch
        n = int(desc_num) - int(asc_num)
        count += 1
        if n == 0:
            break
    return f"count: {count}"
n = int(input("enter number: "))
print(karpekar_constant(n))
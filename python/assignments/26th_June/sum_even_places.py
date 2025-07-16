#program to find sum of even indexed elemnets in a given number
def evn_index_sum(n):
    sum = 0
    for i in range(len(str(n))):
        if i % 2 == 0:
            sum += int(str(n)[i])
    return sum
n = int(input('enter a number: '))
print(evn_index_sum(n))
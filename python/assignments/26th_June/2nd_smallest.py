# find 2nd smallest digit in a number
def find_second_smallest(num):
    arr=[]
    for i in str(num):
        arr.append(int(i))
    uniquely_sorted = sorted(set(arr))
    if len(uniquely_sorted) < 2:
        return "smallest second digit does not exist"
    return uniquely_sorted[1]
num=int(input("enter number: "))
print(find_second_smallest(num))  
    
    
#program to find the smallest and largest elements in a list
def find_smallest_largest(l):
    if len(l) == 0:
        return 'list empty'
    smallest = l[0]
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    return f"smallest: {smallest}\nlargest: {largest}"
l = list(map(int, input("enter space sperated list elements: ").split()))
print(find_smallest_largest(l))
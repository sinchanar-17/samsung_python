#program to remove duplicates in a given list
def remove_duplicates(l):
    new_lst = []
    for i in l:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst
l = list(map(int, input("enter space seperated elements of list: ").split()))
print(remove_duplicates(l))
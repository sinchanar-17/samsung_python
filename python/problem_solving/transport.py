original_list = []
list1_total = int(input("Enter the number of elements in list 1: "))
print("Enter the elements in list 1: ")
for _ in range(list1_total):
    original_list.append(int(input()))

transport_list = []
list2_total = int(input("Enter the number of elements in list 2: "))
print("Enter the elements in list 2: ")
for _ in range(list2_total):
    transport_list.append(int(input()))

i = 0
j = 0

missing_list = []

while i < list1_total and j < list2_total:
    if original_list[i] == transport_list[j]:
        i += 1
        j += 1
    elif original_list[i] != transport_list[j]:
        missing_list.append(original_list[i])
        i += 1

if i < list1_total:
    remaining_elements = original_list[i:]
    for i in remaining_elements:
        missing_list.append(i)

missing_set = set(missing_list)

print(missing_set)
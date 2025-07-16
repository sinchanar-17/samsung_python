# Merge 2  linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data < b.data:
        a.next = merge_sorted_lists(a.next, b)
        return a
    else:
        b.next = merge_sorted_lists(a, b.next)
        return b

def print_list(head):
    while head:
        print(head.data, end=",")
        head = head.next
    print("None")

def create_list(arr):
    head = None
    for value in reversed(arr):
        new_node = Node(value)
        new_node.next = head
        head = new_node
    return head

list1 = create_list([1, 3, 5])
list2 = create_list([2, 4, 6])

print("List 1:")
print_list(list1)
print("List 2:")
print_list(list2)

merged_head = merge_sorted_lists(list1, list2)
print("Merged List:")
print_list(merged_head)
#  Check if 2 SLL converges at some point or not
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def find_intersection(head1, head2):
    len1 = get_length(head1)
    len2 = get_length(head2)

    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next

    while head1 and head2:
        if head1 is head2:
            return head1
        head1 = head1.next
        head2 = head2.next

    return None

def print_result(node):
    if node:
        print("Lists intersect at node with data:", node.data)
    else:
        print("Lists do NOT intersect.")
common = Node(100)
common.next = Node(200)
common.next.next = Node(300)

head1 = Node(10)
head1.next = Node(20)
head1.next.next = common

head2 = Node(5)
head2.next = common


print_result(find_intersection(head1, head2))
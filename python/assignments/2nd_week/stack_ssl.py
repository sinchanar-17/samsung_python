#2. Implement Stack using SLL, insert and delete from front
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackSLL:
    def __init__(self):
        self.top = None  # Also acts as the head of the list

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        popped = self.top.data
        self.top = self.top.next
        print(f"Popped: {popped}")

    def display(self):
        temp = self.top
        print("Stack ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")
s = StackSLL()
s.push(13)
s.push(2)
s.push(98)
s.display()
s.pop()
s.display()
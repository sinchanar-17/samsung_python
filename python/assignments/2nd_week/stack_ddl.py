#3. Implement Stack using DLL, insert and delete from rear
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class StackDLL:
    def __init__(self):
        self.top = None  # Rear of DLL
        self.bottom = None  # Front of DLL

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = self.bottom = new_node
        else:
            self.top.next = new_node
            new_node.prev = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        popped_data = self.top.data
        if self.top == self.bottom:
            self.top = self.bottom = None
        else:
            self.top = self.top.prev
            self.top.next = None
        print(f"Popped: {popped_data}")

    def display(self):
        temp = self.bottom
        print("Bottom ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("Top")
s = StackDLL()
s.push(10)
s.push(900)
s.push(3700)
s.display()
s.pop()
s.display()
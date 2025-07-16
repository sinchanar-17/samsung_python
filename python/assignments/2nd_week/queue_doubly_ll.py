#. Implement Queue using SLL, insert at rear delete from front
class NodeSLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueSLL:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = NodeSLL(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued: {temp.data}")

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")
print("Queue using singly linked list :")
q1 = QueueSLL()
q1.enqueue(67)
q1.enqueue(54)
q1.enqueue(28)
q1.display()
q1.dequeue()
q1.display()
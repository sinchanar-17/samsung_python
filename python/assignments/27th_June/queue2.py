#Implement Queue using list, insert front, delete from rear of the list
import sys as s
queue = []
def enqueue():
    m = int(input("Enter the number you want to add to the queue:"))
    queue.insert(0,m)
    print(f"The element {m} was inserted to the front of the queue successfully.")

def dequeue():
    if len(queue) == 0:
        print("The Queue is empty")
    else:
        popped_element=queue.pop()
        print(f"The element {popped_element} was deleted  from the rear of the  queue.")

def display_queue():
    if len(queue) == 0:
        print("The Queue is empty, nothing to display!")
    else:
        print("The Queue is ",queue)
def exit_queue():
    print("The program ended succesfully!")
    s.exit()
def invalid_input():
    print("Invalid input!,Please enter another choice ")
operations = {1 : enqueue , 
          2 : dequeue ,
          3 : display_queue,
          4 : exit_queue}
while True:
    try :
        print("Choices : \n 1 : enqueue \n 2 : dequeue \n 3 : Display queue \n 4 : Exit Queue")
        choice =int(input("Enter the choice : "))
        operations.get(choice,invalid_input)()
    except ValueError:
        print("Please enter a valid integer")
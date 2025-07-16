#Implement Stack using list, insert and delete from rear of the list
import sys as s
stack = []
choice = 0
def stack_push():
    m=int(input("Enter the number you want to push:"))
    stack.append(m)
    print(f" The element {m} was  pushed succesfully")

def stack_pop():
    if len(stack)==0:
        print("The stack is empty, so we cannot pop")
    else:
        popped_element= stack.pop()
        print(f"The element {popped_element} was poped successfully")

def display_stack():
    print("The stack is ",stack)

def invalid_choice():
    print("Please enter another choice, the choice is incorrect")

def exit_stack():
    print("Program ended succesfully")
    s.exit()
operations = {
    1 : stack_push,
    2 : stack_pop,
    3 : display_stack,
    4 : exit_stack
}
    

while True:
    try:
        print('1 : Stack_push, 2 : Stack_pop, 3 : Display_stack, 4 : Exit' )
        choice =int(input("Enter your choice : "))
        operations.get(choice,invalid_choice)()
    except ValueError:
        print("Enter a valid Integer.")
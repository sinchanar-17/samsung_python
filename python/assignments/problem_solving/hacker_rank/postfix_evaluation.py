stack_lst = []

class Stack:
    def __init__(self, top = -1):
        self.top = top

    def push(self, element):
        stack_lst.append(element) 
        self.top += 1

    def pop(self):
        if self.top != -1:
            stack_lst.pop()
            self.top -= 1
        else:
            print("The stack is Empty!!")

    def display_stack():
        if stack_lst:
            print("The stack elements are ")
            print(stack_lst)
        else:
            print("Stack is Empty!!")

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def show_top(self):
        print("Top value is ", self.top)
        if self.top == -1:
            print("Stack is Empty!!")
        else:
            print("Top element is ", stack_lst[self.top])

    def return_top(self):
        return stack_lst[self.top]

class Checking:
    def operand(self, value):
        if (value >= "A" and value <= "Z") or (value >= "a" and value <= "z") or (value >= "0" and value <= "9"):
            return 1
        else:
            return None
        
    def operator(self, value):
        if (value == "^" or value == "*" or value == "/" or value == "+" or value == "-"):
            return 1
        else:
            return None
        
class PostfixEvaluation:
    def postfix_eval(self, postfix):
        check = Checking()
        stack = Stack()
        i = 0
        while i < len(postfix):
            if check.operand(postfix[i]):
                stack.push(postfix[i])
            elif check.operator(postfix[i]):
                operand2 = int(stack.return_top())
                stack.pop()
                operand1 = int(stack.return_top())
                stack.pop()
                if postfix[i] == "^":
                    stack.push(operand1 ** operand2)
                elif postfix[i] == "*":
                    stack.push(operand1 * operand2)
                elif postfix[i] == "/":
                    stack.push(operand1 / operand2)
                elif postfix[i] == "+":
                    stack.push(operand1 + operand2)
                elif postfix[i] == "-":
                    stack.push(operand1 - operand2)
            i += 1

        result = stack.return_top()
        stack.pop()

        return result
    
if __name__ == '__main__':
    pe = PostfixEvaluation()
    postfix = input("Enter the postfix expression: ")
    result = pe.postfix_eval(postfix)
    print(result)
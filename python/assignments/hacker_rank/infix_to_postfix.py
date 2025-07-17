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
        
    def precedence(self, value):
        if (value == "^"):
            return 3
        elif (value == "*" or value == "/"):
            return 2
        elif (value == "+" or value == "-"):
            return 1
        elif (value == "("):
            return 0
        
class Infixtopostfix:

    def infix_to_postfix(self, infix):
        check = Checking()
        stack = Stack()
        postfix = ""
        i = 0

        while i < len(infix):
            if check.operand(infix[i]):
                postfix += infix[i]
            elif infix[i] == "(":
                stack.push(infix[i])
            elif infix[i] == ")":
                while ((not stack.is_empty()) and stack.return_top() != "("):
                    postfix += stack.return_top()
                    stack.pop()
                stack.pop()
            else:
                if infix[i] == infix[i+1] == "*":
                    infix = list(infix)
                    infix[i:i+2] = "^"
                    infix = ''.join(infix)
                while ((not stack.is_empty()) and check.precedence(infix[i]) < check.precedence(stack.return_top())):
                    postfix += stack.return_top()
                    stack.pop()
                stack.push(infix[i])

            i += 1

        while (not stack.is_empty()):
            postfix += stack.return_top()
            stack.pop()

        return postfix
    
if __name__ == '__main__':
    infix = input("Enter the infix expression: ")

    conversion = Infixtopostfix()

    result = conversion.infix_to_postfix(infix)

    print("The Postfix Expression is", result)
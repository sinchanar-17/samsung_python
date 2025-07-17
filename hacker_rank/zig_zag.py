class Node:
    def __init__(self, data = 0):
        if data == 0:
            data = int(input('Enter data of the node: '))
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        print('An empty BST is created')

    def add_node(self):
        new_node = Node() # create a new Node object
        if self.root == None: # check if the tree is empty
            self.root = new_node
            return
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node

    def in_order(self, temp):
        if temp == None:
            #print('Tree is empty')
            return
        self.in_order(temp.left)
        print(temp.data, end = '  ')
        self.in_order(temp.right)

bst = BST()

bst.add_node()
bst.add_node()
bst.add_node()
bst.in_order(bst.root)
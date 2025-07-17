class Node:
    def __init__(self, data = 0):
        self.left = None
        self.data = data
        self.right = None

class bst:
    def __init__(self):
        self.root = None

    def add_node(self, u, v, direc):
        new_node = Node(u)

        self.root = new_node
        if direc == "R":
            self.root.right = v
        if direc == "L":
            self.root.left = v

bst1 = bst()
bst2 = bst()

n = int(input("enter number of nodes: "))

for i in range((n - 1) + (n - 1)):
    u, v, direc = map(str, input("Enter root and node and the direction: ").split())
    u = int(u)
    v = int(v)

    if i == 0 or i == 1:
        bst1.add_node(u, v, direc)
    else:
        bst2.add_node(u, v, direc)

if bst1.root.left == bst2.root.right and bst1.root.right == bst2.root.left:
    print("YES")
else:
    print("NO")

print(bst1.root.data, bst1.root.right, bst1.root.left)
print(bst2.root.data, bst2.root.right, bst2.root.left)
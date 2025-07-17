class Node:
    def __init__(self, key, color="R"):
        self.key = key
        self.color = color  # "R" or "B"
        self.left = None
        self.right = None
        self.parent = None

# Sentinel NIL node
NIL_LEAF = Node(key=None, color="B")

# Fix parent references
def set_parent(child, parent):
    if child and child != NIL_LEAF:
        child.parent = parent

# Left Rotate
def left_rotate(root, x):
    y = x.right
    x.right = y.left
    set_parent(y.left, x)

    y.parent = x.parent
    if x.parent is None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y
    return root

# Right Rotate
def right_rotate(root, y):
    x = y.left
    y.left = x.right
    set_parent(x.right, y)

    x.parent = y.parent
    if y.parent is None:
        root = x
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x

    x.right = y
    y.parent = x
    return root

# Fix RBT after insertion
def fix_insert(root, z):
    while z.parent and z.parent.color == "R":
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y and y.color == "R":
                z.parent.color = "B"
                y.color = "B"
                z.parent.parent.color = "R"
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    root = left_rotate(root, z)
                z.parent.color = "B"
                z.parent.parent.color = "R"
                root = right_rotate(root, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y and y.color == "R":
                z.parent.color = "B"
                y.color = "B"
                z.parent.parent.color = "R"
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    root = right_rotate(root, z)
                z.parent.color = "B"
                z.parent.parent.color = "R"
                root = left_rotate(root, z.parent.parent)
    root.color = "B"
    return root

# Insert into RBT
def insert(root, key):
    z = Node(key)
    z.left = z.right = NIL_LEAF
    y = None
    x = root

    while x and x != NIL_LEAF:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right

    z.parent = y
    if y is None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

    return fix_insert(root, z)

# In-order traversal
def inorder(node):
    if node and node != NIL_LEAF:
        inorder(node.left)
        print(f"{node.key}({node.color})", end=' ')
        inorder(node.right)

# Main
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    global NIL_LEAF
    root = None

    for val in arr:
        node = Node(val)
        node.left = node.right = NIL_LEAF
        root = insert(root, val)

    inorder(root)
    print()

if __name__ == "__main__":
    main()

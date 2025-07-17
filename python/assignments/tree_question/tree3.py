class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Helper functions
def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

# Rotations with print statements
def right_rotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    update_height(z)
    update_height(y)

    print(f"LL Rotation at node {z.key}")
    return y

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    update_height(z)
    update_height(y)

    print(f"RR Rotation at node {z.key}")
    return y

def left_right_rotate(z):
    z.left = left_rotate(z.left)
    print(f"LR Rotation at node {z.key}")
    return right_rotate(z)

def right_left_rotate(z):
    z.right = right_rotate(z.right)
    print(f"RL Rotation at node {z.key}")
    return left_rotate(z)

# AVL Insertion with Rotation Reporting
def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    update_height(root)
    balance = get_balance(root)

    # Balance conditions
    if balance > 1 and key < root.left.key:
        return right_rotate(root)  # LL
    if balance < -1 and key > root.right.key:
        return left_rotate(root)   # RR
    if balance > 1 and key > root.left.key:
        return left_right_rotate(root)  # LR
    if balance < -1 and key < root.right.key:
        return right_left_rotate(root)  # RL

    return root

# Main logic
def main():
    N = int(input())
    values = list(map(int, input().split()))

    root = None
    for val in values:
        root = insert(root, val)

if __name__ == "__main__":
    main()

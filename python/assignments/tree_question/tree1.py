class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(root):
    if not root:
        return 0
    return root.height


def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)


def right_rotate(y):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Get balance factor
    balance = get_balance(root)

    # Balance the tree
    # Case 1 - Left Left
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Case 2 - Right Right
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Case 3 - Left Right
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Case 4 - Right Left
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def preorder_traversal(root):
    if not root:
        return []
    return [root.key] + preorder_traversal(root.left) + preorder_traversal(root.right)


# Main execution
if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    root = None
    for val in values:
        root = insert(root, val)

    print(*preorder_traversal(root))

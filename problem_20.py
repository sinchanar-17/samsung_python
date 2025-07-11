class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_node(root, val):
    # If the tree is empty, create the root node.
    if root is None:
        return TreeNode(val)
    
    # If the value is less than the current node's value, insert into the left subtree.
    if val < root.val:
        root.left = insert_node(root.left, val)
    # If the value is greater than or equal to the current node's value, insert into the right subtree.
    else:
        root.right = insert_node(root.right, val)
    return root

def height_of_tree(root):
    # Base case: If the node is None, it means the end of a leaf, so return -1.
    if root is None:
        return -1

    # Recursively find the height of the left subtree.
    left_height = height_of_tree(root.left)

    # Recursively find the height of the right subtree.
    right_height = height_of_tree(root.right)

    # The height of the current node is 1 (for the current node itself)
    # plus the maximum height of its left or right subtree.
    return max(left_height, right_height) + 1

# Input values for the nodes.
node_values = [4, 2, 6, 1, 3, 5, 7] # This order helps create a more balanced tree

# Build the binary search tree.
root = None
for val in node_values:
    root = insert_node(root, val)

# Calculate the height of the tree.
tree_height = height_of_tree(root)

# Print the result.
print("Height of the binary tree:", tree_height)

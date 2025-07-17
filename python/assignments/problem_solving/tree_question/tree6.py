class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(relations):
    nodes = {}
    has_parent = set()

    for val, l, r in relations:
        if val not in nodes:
            nodes[val] = Node(val)
        if l != -1:
            if l not in nodes:
                nodes[l] = Node(l)
            nodes[val].left = nodes[l]
            has_parent.add(l)
        if r != -1:
            if r not in nodes:
                nodes[r] = Node(r)
            nodes[val].right = nodes[r]
            has_parent.add(r)

    # Root is the node that is not anyone's child
    for val in nodes:
        if val not in has_parent:
            return nodes[val]  # root

    return None

def search_rbt(root, key):
    current = root
    while current:
        if current.val == key:
            return "Found"
        elif key < current.val:
            current = current.left
        else:
            current = current.right
    return "Not Found"

# Driver Code
def main():
    n = int(input())
    relations = []
    for _ in range(n):
        vals = list(map(int, input().split()))
        relations.append((vals[0], vals[1], vals[2]))
    k = int(input())

    root = build_tree(relations)
    print(search_rbt(root, k))

if __name__ == "__main__":
    main()

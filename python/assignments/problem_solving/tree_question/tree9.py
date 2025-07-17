import math
from collections import deque

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.leaf = leaf
        self.keys = []
        self.children = []

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == (2 * self.t - 1):
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

class BTree:
    def __init__(self, m):
        self.t = math.ceil(m / 2)
        self.root = BTreeNode(self.t, True)

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            s = BTreeNode(self.t, False)
            s.children.insert(0, root)
            s.split_child(0)
            i = 0
            if key > s.keys[0]:
                i += 1
            s.children[i].insert_non_full(key)
            self.root = s
        else:
            root.insert_non_full(key)

    def level_order_traversal(self):
        result = []
        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            level_keys = []
            for _ in range(level_size):
                node = queue.popleft()
                level_keys.extend(node.keys)
                if not node.leaf:
                    queue.extend(node.children)
            print(' '.join(map(str, level_keys)))

# Main function to read input and drive the insertion
def main():
    n, m = map(int, input().split())
    keys = list(map(int, input().split()))

    tree = BTree(m)
    for key in keys:
        tree.insert(key)

    tree.level_order_traversal()

if __name__ == "__main__":
    main()

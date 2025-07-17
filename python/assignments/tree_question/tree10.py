from collections import deque

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

    def find_key(self, key):
        for i, item in enumerate(self.keys):
            if key <= item:
                return i
        return len(self.keys)

    def remove(self, key):
        idx = self.find_key(key)

        if idx < len(self.keys) and self.keys[idx] == key:
            if self.leaf:
                self.keys.pop(idx)
            else:
                self.remove_from_non_leaf(idx)
        else:
            if self.leaf:
                return  # Key not found
            flag = (idx == len(self.keys))
            if len(self.children[idx].keys) < self.t:
                self.fill(idx)
            if flag and idx > len(self.keys):
                self.children[idx - 1].remove(key)
            else:
                self.children[idx].remove(key)

    def remove_from_non_leaf(self, idx):
        key = self.keys[idx]
        if len(self.children[idx].keys) >= self.t:
            pred = self.get_predecessor(idx)
            self.keys[idx] = pred
            self.children[idx].remove(pred)
        elif len(self.children[idx + 1].keys) >= self.t:
            succ = self.get_successor(idx)
            self.keys[idx] = succ
            self.children[idx + 1].remove(succ)
        else:
            self.merge(idx)
            self.children[idx].remove(key)

    def get_predecessor(self, idx):
        cur = self.children[idx]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def get_successor(self, idx):
        cur = self.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def fill(self, idx):
        if idx != 0 and len(self.children[idx - 1].keys) >= self.t:
            self.borrow_from_prev(idx)
        elif idx != len(self.keys) and len(self.children[idx + 1].keys) >= self.t:
            self.borrow_from_next(idx)
        else:
            if idx != len(self.keys):
                self.merge(idx)
            else:
                self.merge(idx - 1)

    def borrow_from_prev(self, idx):
        child = self.children[idx]
        sibling = self.children[idx - 1]
        child.keys.insert(0, self.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        self.keys[idx - 1] = sibling.keys.pop()

    def borrow_from_next(self, idx):
        child = self.children[idx]
        sibling = self.children[idx + 1]
        child.keys.append(self.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        self.keys[idx] = sibling.keys.pop(0)

    def merge(self, idx):
        child = self.children[idx]
        sibling = self.children[idx + 1]
        child.keys.append(self.keys.pop(idx))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        self.children.pop(idx + 1)

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def build_from_level_order(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(key)
        else:
            if len(self.root.keys) == (2 * self.t - 1):
                s = BTreeNode(self.t, False)
                s.children.append(self.root)
                s.split_child = self.split_child
                s.split_child(0)
                i = 0
                if key > s.keys[0]:
                    i += 1
                s.children[i].insert_non_full = self.insert_non_full
                s.children[i].insert_non_full(key)
                self.root = s
            else:
                self.root.insert_non_full = self.insert_non_full
                self.root.insert_non_full(key)

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

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and self.keys[i] > key:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and self.keys[i] > key:
                i -= 1
            i += 1
            if len(self.children[i].keys) == (2 * self.t - 1):
                self.split_child = BTree.split_child.__get__(self)
                self.children[i].split_child = self.split_child
                self.split_child(i)
                if self.keys[i] < key:
                    i += 1
            self.children[i].insert_non_full = self.insert_non_full
            self.children[i].insert_non_full(key)

    def delete(self, key):
        if not self.root:
            return
        self.root.remove(key)
        if len(self.root.keys) == 0:
            if self.root.leaf:
                self.root = None
            else:
                self.root = self.root.children[0]

    def level_order(self):
        if not self.root:
            return "Empty"
        result = []
        q = deque([self.root])
        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                result.extend(node.keys)
                if not node.leaf:
                    q.extend(node.children)
        return ' '.join(map(str, result))

# Main function to execute the problem
def main():
    n, t = map(int, input().split())
    initial_keys = list(map(int, input().split()))
    q = int(input())
    delete_keys = list(map(int, input().split()))

    bt = BTree(t)
    bt.build_from_level_order(initial_keys)

    for key in delete_keys:
        bt.delete(key)
        print(bt.level_order())

if __name__ == "__main__":
    main()

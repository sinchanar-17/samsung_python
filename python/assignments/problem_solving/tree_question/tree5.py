from collections import deque

class Node:
    def __init__(self, key, color, parent=None):
        self.key = key
        self.color = color  # 'R' or 'B'
        self.left = None
        self.right = None
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, 'B')  # Sentinel NIL node
        self.root = self.NIL

    def build_tree(self, keys, colors):
        # BFS build based on level order
        nodes = [Node(k, c) for k, c in zip(keys, colors)]
        for node in nodes:
            node.left = self.NIL
            node.right = self.NIL
        if not nodes:
            return
        self.root = nodes[0]
        queue = deque([self.root])
        idx = 1
        while queue and idx < len(nodes):
            current = queue.popleft()
            if idx < len(nodes):
                current.left = nodes[idx]
                nodes[idx].parent = current
                queue.append(nodes[idx])
                idx += 1
            if idx < len(nodes):
                current.right = nodes[idx]
                nodes[idx].parent = current
                queue.append(nodes[idx])
                idx += 1

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete_node(self, key):
        z = self.search(self.root, key)
        if z == self.NIL:
            return  # Key not found
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'B':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'B' and w.right.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.right.color == 'B':
                        w.left.color = 'B'
                        w.color = 'R'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.right.color = 'B'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'B' and w.left.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.left.color == 'B':
                        w.right.color = 'B'
                        w.color = 'R'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.left.color = 'B'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'B'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def search(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.sea

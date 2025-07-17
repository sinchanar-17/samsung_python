class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store word at end node for easy retrieval

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word

def findWords(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    m, n = len(board), len(board[0])
    result = set()
    visited = [[False]*n for _ in range(m)]

    def dfs(r, c, node):
        char = board[r][c]
        if char not in node.children:
            return
        next_node = node.children[char]
        if next_node.word:
            result.add(next_node.word)

        visited[r][c] = True
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                dfs(nr, nc, next_node)
        visited[r][c] = False

    for i in range(m):
        for j in range(n):
            dfs(i, j, trie.root)

    return result

# Driver code
def main():
    m, n = map(int, input().split())
    board = []
    for _ in range(m):
        board.append(input().split())

    k = int(input())
    words = [input().strip() for _ in range(k)]

    results = findWords(board, words)
    for word in results:
        print(word)

if __name__ == "__main__":
    main()

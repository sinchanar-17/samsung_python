class TrieNode:
    def __init__(self):
        self.children = {}  # Maps character to TrieNode
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end_of_word

    def startsWith(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

# Driver code
def main():
    n = int(input())
    trie = Trie()
    for _ in range(n):
        command = input().strip().split()
        if command[0] == "insert":
            trie.insert(command[1])
        elif command[0] == "search":
            print("true" if trie.search(command[1]) else "false")
        elif command[0] == "startsWith":
            print("true" if trie.startsWith(command[1]) else "false")

if __name__ == "__main__":
    main()

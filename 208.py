class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def prefixNode(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        node = self.prefixNode(word)
        if not node:
            return False
        else:
            return node.end == True

    def startsWith(self, prefix):
        node = self.prefixNode(prefix)
        if not node:
            return False
        return True

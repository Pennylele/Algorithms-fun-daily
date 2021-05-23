class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.end = True  

        
    def searchNode(self, node, word):
        if not word:
            if node.end:
                self.found = True
            return
        
        elif word[0] == ".":
            for n in node.children.values(): # IMPORTANT - seems like we need to add .values() here, otherwise the node.children would return a defaultdict object rather than the keys.
                #print(node.children, node.children.values())
                self.searchNode(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.searchNode(node, word[1:])
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.found = False
        self.searchNode(node, word)
        return self.found
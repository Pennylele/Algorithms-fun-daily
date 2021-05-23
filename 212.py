class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True
        
class Solution:
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root # interesting
        for word in words:
            trie.insert(word)
            
        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                self.dfs(i, j, node, board, "", res)
        return res
    
    def dfs(self, r, c, node, board, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False 
            '''since we already completed that word and added in our result array, we don't want to get duplicates of that word so we set it to False.
Example ['aaa','aaab'] after adding 'aaa' when we search for 'aaab' we will add 'aaa' again if we don't set it to False, so we avoid that by setting it to False.'''
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return
        
        tmp = board[r][c]
        node = node.children.get(tmp)
        if not node:
            return
        
        board[r][c] = "#"
        self.dfs(r+1, c, node, board, path+tmp, res)
        self.dfs(r-1, c, node, board, path+tmp, res)
        self.dfs(r, c+1, node, board, path+tmp, res)
        self.dfs(r, c-1, node, board, path+tmp, res)
        board[r][c] = tmp
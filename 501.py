# I think even the recursive function is very trivial
class TreeNode():
    def __init__(self):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root):
        self.prev, self.MAX, self.cur, self.res = None, 0, 0, []
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.cur = 1 if self.prev != node.val else self.cur + 1
        if self.cur == self.MAX:
            self.res.append(node.val)
        if self.cur > self.MAX:
            self.res = [node.val]
            self.MAX = self.cur
        self.prev = node.val
        self.dfs(node.right)

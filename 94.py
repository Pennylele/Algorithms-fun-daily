class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        res = []
        dfs(root)
        return res

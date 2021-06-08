# Input: root = [1,2,2,3,4,4,3]
# Output: true
#    1
#   / \
#  2   2
# / \ / \
# 3 4 4 3
# DFS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):
        if left and right:
            return left.val == right.val and self.dfs(left.left) == self.dfs(right.right) and self.dfs(left.right) == self.dfs(right.left)
        return left == right
#/////////////////////////BFS//////////////////////////////
class Solution:
    def isSymmetric(self, root):
        if not root: return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            elif not left or not right or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True


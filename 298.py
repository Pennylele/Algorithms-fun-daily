# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def longest_path(node):
            if not node: return 0
            
            length = 1 # Have to be clear that this length is changing along the stack. That's why we need self.longestPath
            left = longest_path(node.left)
            right = longest_path(node.right)
            if node.left and node.left.val == node.val + 1:
                length = max(length, left + 1)
            if node.right and node.right.val == node.val + 1:
                length = max(length, right + 1)
            self.longestPath = max(self.longestPath, length)
            return length
        
        self.longestPath = 0
        longest_path(root)
        return self.longestPath
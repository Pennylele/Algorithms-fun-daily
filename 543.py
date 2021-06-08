# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# I think for each node should always be returned the largest value from the left and the right. The answer would be max(left, right, left+right)
class Solution:
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.MAX = max(left+right, self.MAX)
            return 1 + max(left, right)
            
        self.MAX = 0
        dfs(root)
        return self.MAX


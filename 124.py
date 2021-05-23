# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# for the current node, we add the max of the left and right children.
# test case: [2,-1] => why max(dfs(node.left). 0) is important.
class Solution:
    def maxPathSum(self, root):
        if not root: return None
        self.ans = float('-inf')
  
        def dfs(node):
            if not node: return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.ans = max(self.ans, left + right + node.val)
            return max(left, right) + node.val

        dfs(root)
        return self.ans
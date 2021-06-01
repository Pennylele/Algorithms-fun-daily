class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node: return 0
            if low <= node.val <= high:
                self.ans += node.val
            if node.val > low: # if node.val < low, we stop traversing to the left
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
            
        self.ans = 0
        dfs(root)
        return self.ans
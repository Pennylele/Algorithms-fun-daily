#    10
#    / \
#   5  12
#  /\  /\
# 3 6 11 13
class Solution:
    def isValidBST(self, root):
        def dfs(node, MIN, MAX):
            if not node: return True # Don't forget about this base case
            if node.val >= MAX or node.val <= MIN:
                return False
            left = dfs(node.left, MIN, node.val)
            right = dfs(node.right, node.val, MAX)
            return left and right

        MIN, MAX = float('-inf'), float('inf')
        return dfs(root, MIN, MAX)
        

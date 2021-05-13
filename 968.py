# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#/////////////////////////////////
# Basically, this is a greedy method where the node info is passed on from bottom to up
# We want the parent node of the leaves to install cams.
# 0 means this node is a leaf 
# 1 means this node a parent (of a leaf) and has the cam 
# 2 means this node is covered without a cam
# SCENARIOS
# 1. if a node's child is a leaf, we return 1 to the parent node (needing a camera)
# 2. if the node's child has a cam (1), return 2 (being covered)
# 3. if a node's child is 1, return to the parent 2 (cause its child has a cam)
# 4. if a node's child is not 1, not 0, but 2, that's the leaf nodes.
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 2
            l, r = dfs(node.left), dfs(node.right)
            if l == 0 or r == 0:
                self.res += 1 # we need a camera for its parent
                return 1
            return 2 if l == 1 or r == 1 else 0 # returning 0 is when both nodes are 2
        return (dfs(root) == 0) + self.res # if dfs(root) == 0 means this tree only has 1 node and we need a cam on it.
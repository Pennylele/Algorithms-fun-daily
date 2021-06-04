# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        self.preIdx, self.postIdx = 0, 0
        
        def helper():
            root = TreeNode(pre[self.preIdx])
            self.preIdx += 1
            if root.val != post[self.postIdx]:
                root.left = helper()
            if root.val != post[self.postIdx]:
                root.right = helper()
            self.postIdx += 1
            return root
        
        return helper()
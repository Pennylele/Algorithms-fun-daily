# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# sorted array should be inorder traversal of the BST. Probably should use Binary search, so that we can balance the left and right subtrees.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def helper(l, r):
            if l > r: return None
            mid = l + (r-l)//2
            root_val = nums[mid]
            root = TreeNode(root_val)
            root.left = helper(l, mid-1)
            root.right = helper(mid+1, r)
            return root
        
        helper(0, len(nums)-1)


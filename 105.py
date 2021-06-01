class Solution:
    def buildTree(self, preorder, inorder):
        def helper(l, r):
            nonlocal preorder_index
            if l > r: return None # return None is important to get back to the previous level
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)

            preorder_index += 1
            root.left = helper(l, hashmap[root_val]-1) # (0, -1)
            root.right = helper(hashmap[root_val]+1, r) # (1, 0)
            return root
        
        preorder_index = 0
        hashmap = {}
        for idx, val in enumerate(inorder):
            hashmap[val] = idx
        
        n = len(inorder)
        return helper(0, n-1)
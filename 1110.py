class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete_set = set(to_delete)

        def helper(node, root_removed):
            if not node:
                return None
            delete_flag = node.val in to_delete_set
            if root_removed and not delete_flag:
                res.append(node)
            node.left = helper(node.left, delete_flag)
            node.right = helper(node.right, delete_flag)
            return None if delete_flag else node # This is my weaknest place to understand...
                
        
        helper(root, True)
        return res
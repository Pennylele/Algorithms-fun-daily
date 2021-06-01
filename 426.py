class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        def helper(node):
            nonlocal first, last
            if node:
                helper(node.left)
                if not last:
                    first = node
                else:
                    last.right = node
                    node.left = last
                last = node
                helper(node.right)
        
        if not root:
            return None
        
        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first
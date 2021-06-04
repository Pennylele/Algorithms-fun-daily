# Method 1: flatten the BST into an array. Then it's easier just to process on the array
# Method 2: in order to achieve a memory of O(h), close enough, we can create a customized inorder traversal by using a stack, and continuingly traverse left
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.__leftmost_inorder(root)
        
    def __leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        

    def next(self) -> int:
        nxt_node = self.stack.pop()
        
        if nxt_node.right:
            self.__leftmost_inorder(nxt_node.right)
        
        return nxt_node.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
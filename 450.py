# search BST until we find the node to delete
# find this node's predecessor -> then recursively remove nodes
# If not predecessor, then find the successor -> recursively remove nodes
class TreeNode:
    def __init__(self, val=0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findPredecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val
    
    def findSuccessor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def deleteNode(self, root, key):
        if not root: return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right: # This is when this root is already a leaf
                return None
            elif root.right:
                root.val = self.findSuccessor(root) # change the current node'v value to its predecessor
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root.val = self.findPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
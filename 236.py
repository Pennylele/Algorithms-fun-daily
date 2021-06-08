# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

#     3
#    / \
#   5   1
#  / \ / \
# 6  2 0  8
#   / \
#  7   4
 # example: if p is in the left subtree and q is in the right subtree, the LCA should be the root
 # If they are both in the same substree, then one of them should be the anscester.
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in {None, p, q}:
            return root
        left = lowestCommonAncestor(root.left, p, q)
        right = lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right



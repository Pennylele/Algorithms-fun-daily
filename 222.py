# O(logn) - for complete binary tree
class Solution:
    def countNodes(self, root):

        # Trying to check if the leave node of index pivot can be found (binary search too)
        def searchNode(pivot, node):
            left, right = 0, 2 ** height - 1
            
            for i in range(height): # IMPORTANT: we only go "height" rounds of traversals.
                mid = left + (right - left) // 2
                if pivot <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            
            return node if node else None

        # Calculating the height
        height = 0
        dummy = root
        while dummy and dummy.left:
            dummy = dummy.left # don't write the bug, please
            height += 1
        
        # index the complete node from 0 to 2 ** height (binary search)
        l, r = 0, 2 ** height - 1
        while l <= r:
            pivot = l + (r - l) // 2
            if searchNode(pivot, root):
                l = pivot + 1
            else:
                r = pivot - 1
        
        return l + 2 ** height - 1


# O(n)
class Solution:
    def countNodes(self, root):
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0


class Solution:
    def connect(self, root):
        if not root or not root.left:
            return root
        cur = root
        nxt = root.left

        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = nxt
                nxt = cur.left
        return root
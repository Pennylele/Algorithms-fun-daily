class Solution:
    def isSameTree(self, p, q):
        if not p and not q: 
            return True
        if (not p and q) or (not q and p):
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

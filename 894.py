# Initial - every node has 2 options: either 0 or 2 children.
# recursion relations - base case - whenever n nodes are used, we append the root node to the ans list
# time complexity - 2^N

class Solution:
    def __init__(self):
        self.memo = {}
        self.memo[0] = []
        self.memo[1] = [TreeNode(0)]
        
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        ans = [] # we need this ans to be dynamic. It gets overwritten everytime the ans is returned to the previous level.
        
        if n in self.memo:
            return self.memo[n]
        
        for i in range(1, n, 2):
            left_tree = self.allPossibleFBT(i)
            right_tree = self.allPossibleFBT(n-1-i)
            
            for left in left_tree: # if this is hard to think - use the example of a 3-node tree.
                for right in right_tree:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    
                    ans.append(root)
        
        self.memo[n] = ans
        
        return ans
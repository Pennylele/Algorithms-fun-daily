# This problem basically means to find the minimum length string that contains all the possible combinations out of the k digits. The password's length is n which is basically the permutation length.
# Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.
# We can think of this problem as the problem of finding an Euler path (a path visiting every edge exactly once) on the following graph: there are k^(n-1) nodes with each node having k edges.
# We will modify our standard depth-first search: instead of keeping track of nodes, we keep track of (complete) edges: seen records if an edge has been visited.
class Solution:
    def crackSafe(self, n, k):
        self.visited = set()
        self.ans = ""

        def dfs(start):
            for i in map(str, range(k)):
                nei = start + i
                if nei not in self.visited:
                    self.visited.add(nei)
                    dfs(nei[1:])
                    self.ans += i
        
        start = "0" * (n-1)
        dfs(start)
        return self.ans + "0" * (n-1)

obj = Solution()
print(obj.crackSafe(2, 2))


class Solution:
    def getMaximumGold(self, grid):
        def dfs(r, c, gold):
            if 0 <= r < R and 0 <= c < C and (r, c) not in self.visited and grid[r][c] != 0:
                self.visited.add((r, c))
                gold = grid[r][c] + max(dfs(r+1, c, gold), dfs(r-1, c, gold), dfs(r, c+1, gold), dfs(r, c-1, gold))
                self.visited.remove((r,c))
                return gold
            return 0

        R, C = len(grid), len(grid[0])
        MAX = 0
        self.visited = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] != 0:
                    MAX = max(MAX, dfs(i, j, 0))
        return MAX

obj = Solution()
grid = [[0,6,0],[5,8,7],[0,9,0]]
print(obj.getMaximumGold(grid))
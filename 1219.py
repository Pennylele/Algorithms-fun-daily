class Solution:
    def getMaximumGold(self, grid):
        # dfs function
        def dfs(row, col, gold):
            if not (0 <= row < R and 0 <= col < C and (row, col) not in self.visited and grid[row][col] != 0):
                return 0
            self.visited.add((row, col))
            gold = max(gold, grid[row][col] + max(dfs(row+1, col, gold), dfs(row-1, col, gold), dfs(row, col+1, gold), dfs(row, col-1, gold)))
            self.visited.remove((row, col))
            self.max_gold = max(self.max_gold, gold)
            return gold


        # start the search from a non-0 cell
        self.max_gold = 0
        self.visited = set()
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        return self.max_gold

obj = Solution()
grid = [[0,6,0],[5,8,7],[0,9,0]]
print(obj.getMaximumGold(grid))
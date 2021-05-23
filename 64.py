class Solution:
    def minPathSum(self, grid):
        R, C = len(grid), len(grid[0])
        # calculate the first row's min path values
        for i in range(1, C):
            grid[0][i] += grid[0][i-1]
        # calculate the first col's min path values
        for j in range(1, R):
            grid[j][0] += grid[j-1][0]
        # filling in the rest
        for i in range(1, R):
            for j in range(1, C):
                grid[i][j] = min(grid[i][j] + grid[i-1][j], grid[i][j] + grid[i][j-1])
        return grid[-1][-1]
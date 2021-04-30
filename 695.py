# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
class Solution:
    def maxAreaOfIsland(self, grid):
        def dfs(row, col):
            if 0 <= row < R and 0 <= col < C and (row, col) not in self.visited and grid[row][col] == 1:
                self.visited.add((row, col))
                return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
            else:
                return 0


        R, C = len(grid), len(grid[0])
        self.visited = set()
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans

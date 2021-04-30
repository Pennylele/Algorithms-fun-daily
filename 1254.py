# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
class Solution:
    def closedIsland(self, grid):
        def dfs(row, col):
            if row < 0 or row >= R or col < 0 or col >= C:
                return False
            if grid[row][col] == 1:
                return True
            
            grid[row][col] = 1
            left = dfs(row, col-1)
            up = dfs(row-1, col)
            right = dfs(row, col+1)
            down = dfs(row+1, col)

            return left and up and right and down

            
        R, C = len(grid), len(grid[0])

        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    ans += dfs(i, j)
        return ans
#///////////////////////////////////////////////////////////
class Solution:
    def closedIsland(self, grid):
        def dfs(row, col):
            if grid[row][col] == 0 and (row == R-1 or row == 0 or col == C-1 or col == 0):
                self.flag = False
            for new_row, new_col in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if 0 <= new_row < R and 0 <= new_col < C and grid[new_row][new_col] == 0 and (new_row, new_col) not in self.visited:
                    self.visited.add((new_row, new_col))
                    dfs(new_row, new_col)

            
        R, C = len(grid), len(grid[0])

        ans = 0
        self.visited = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0 and (i, j) not in self.visited:
                    self.flag = True
                    dfs(i, j)
                    if self.flag: ans += 1
        return ans

s = Solution()
print(s.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
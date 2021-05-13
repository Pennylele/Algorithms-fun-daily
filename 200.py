class Solution:
    def numIslands(self, grid):
        R, C = len(grid), len(grid[0])

        def dfs(row, col):
            self.visited.add((row, col))
            for new_r, new_c in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if 0 <= new_r < R and 0 <= new_c < C and (new_r, new_c) not in self.visited and grid[new_r][new_c] == '1':
                    dfs(new_r, new_c)
            return

        ans = 0
        self.visited = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1' and (i, j) not in self.visited:
                    dfs(i, j)
                    ans += 1
        return ans

obj = Solution()
print(obj.numIslands(
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

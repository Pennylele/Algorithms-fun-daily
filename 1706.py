class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        
        ans = []
        for c in range(C):
            x = c
            for r in range(R):
                slope = grid[r][x]
                x += slope
                if x < 0 or x > C-1 or grid[r][x] != slope:
                    ans.append(-1)
                    break
            else:
                ans.append(x)
        return ans
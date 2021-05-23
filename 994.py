# Question: how many 2s we have in the grid? 
# grid = 
# [[2,1,1],
#  [1,1,0],
#  [0,1,2]]
# I think we just need to find 2s and change their neighbors to 2 as well. Using BFS to count the minutes.
# The solution is kinda smart - I didn't think of it - using (-1, -1) to mark one level of rotten process.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_q = collections.deque()
        fresh = 0
        R, C = len(grid), len(grid[0])
        
        # counting original rotten oranges.
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    rotten_q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        # BFS to count rounds
        rotten_q.append((-1, -1))
        minutes = -1
        while rotten_q:
            row, col = rotten_q.popleft() # kinda have this tendency of forgetting to write popleft()
            if row == -1:
                minutes += 1
                if rotten_q: # IMPORTANT!! To avoid infinite loop
                    rotten_q.append((-1, -1))
            
            else:
                for new_r, new_c in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                    if 0 <= new_r < R and 0 <= new_c < C and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        rotten_q.append((new_r, new_c))
        
        return minutes if fresh == 0 else -1 # [Edge Case]: The fresh oranges count is used here to avoid the failed attempt to rotten all oranges.
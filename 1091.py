# Shortest path by intuition is BFS
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        R, C = len(grid), len(grid[0])
        q = collections.deque([(0, 0, 1)])
        visited = set()
        while q:
            r, c, step = q.popleft()
            if r == R-1 and c == C-1:
                return step
            for (new_r, new_c) in (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c-1), (r+1, c-1), (r-1, c+1):
                if 0 <= new_r < R and 0 <= new_c < C and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                    visited.add((new_r, new_c))
                    q.append((new_r, new_c, step + 1))
        return -1
# Or we can just start from (-1, -1)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        q = [(-1, -1, 0)]
        
        for i, j, d in q:
            if i == n-1 and j == n-1: 
                return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    q.append((x,y,d+1))
        return -1
        

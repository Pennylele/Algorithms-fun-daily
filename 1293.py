class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])        
        q = collections.deque([(0, 0, k)])        
        self.visited = set()
        steps = 0
        
        while q:
            for _ in range(len(q)):
                r, c, k = q.popleft()
                
                if r == R-1 and c == C-1:
                    return steps
                
                for new_r, new_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= new_r < R and 0 <= new_c < C:
                        if grid[new_r][new_c] == 1 and k > 0 and (new_r, new_c, k-1) not in self.visited:
                            q.append((new_r, new_c, k-1))
                            self.visited.add((new_r, new_c, k-1))
                        elif grid[new_r][new_c] == 0 and (new_r, new_c, k) not in self.visited:
                            q.append((new_r, new_c, k))
                            self.visited.add((new_r, new_c, k))                        
                            
            steps += 1
        
        return -1
# Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 7
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
# Wow complex... We need a few variables:
# hits: how many times the 0 can be reached from a 1
# disSum: how many steps can this 0 be reached by all 1s
# visited (for each 1): for each round of BFS
# buildings: checkpoint - how many buildings are there in the map
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        hits, disSum = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]
        buildings = sum([grid[i][j] for i in range(R) for j in range(C) if grid[i][j] == 1])
        
        def bfs(row, col):
            visited = {(row, col)}
            count1 = 1
            q = collections.deque([(row, col, 0)])
            while q:
                r, c, distance = q.popleft()
                for new_r, new_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= new_r < R and 0 <= new_c < C and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        if grid[new_r][new_c] == 0:
                            #visited.add((new_r, new_c))
                            q.append((new_r, new_c, distance + 1))
                            hits[new_r][new_c] += 1
                            disSum[new_r][new_c] += distance + 1
                        elif grid[new_r][new_c] == 1:
                            count1 += 1

            return count1 == buildings                            
            
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    if not bfs(i, j): return -1
        return min([disSum[i][j] for i in range(R) for j in range(C) if grid[i][j] == 0 and hits[i][j] == buildings] or [-1])
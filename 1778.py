# So we could use DFS + BFS for this problem. The reason to use DFS first to map out the grid, I think is because we want to avoid using too much memory by running BFS especially if such path doesn't exist. So at least in DFS, we can quickly map out the bigger picture and rule out all the blocked cells. So that the BFS can be faster and use less memory overall..
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:        
        directions = {'L': (0, -1), 'U': (-1, 0), 'R': (0, 1), 'D': (1, 0)}
        anti_d = {'L': 'R', 'U': 'D', 'R': 'L', 'D': 'U'}
        isValid = {}
        isValid[(0, 0)] = master.isTarget()
        
        # DFS to map out the target location as well as the valid cells (rulling not the blocked cells)
        def dfs(r, c):
            for d in directions:
                new_r, new_c = r + directions[d][0], c + directions[d][1]
                if (new_r, new_c) not in isValid and master.canMove(d):
                    master.move(d) # Don't forget to move to the d
                    isValid[(new_r, new_c)] = master.isTarget()
                    dfs(new_r, new_c)
                    master.move(anti_d[d]) # Don't forget to backtrack
                
        dfs(0, 0)
        
        # BFS to find the shortest path
        q = collections.deque([(0, 0, 0)])
        self.visited = set()
        while q:
            for _ in range(len(q)):
                r, c, step = q.popleft()
                if isValid[(r, c)] == True:
                    return step
                for new_r, new_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if (new_r, new_c) in isValid and (new_r, new_c) not in self.visited:
                        self.visited.add((new_r, new_c))
                        q.append((new_r, new_c, step + 1))
        return -1
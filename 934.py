# The result should be: we can reach any island from any island
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        self.seen = set()
        
        # Start DFS
        def first_round():
            for i in range(R):
                for j in range(C):
                    if A[i][j] == 1:
                        return i, j
        
        # DFS to get the 1st island
        row, col = first_round()
        self.seen.add((row, col))
        
        def dfs(row, col):
            for new_row, new_col in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if 0 <= new_row < R and 0 <= new_col < C and (new_row, new_col) not in self.seen and A[new_row][new_col] == 1:
                    self.seen.add((new_row, new_col))
                    dfs(new_row, new_col)
       
        dfs(row, col)

        # Then use BFS to find the shortest path
        q = collections.deque(self.seen)
        distance = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if A[row][col] == 1 and distance > 0:
                    return distance - 1
                
                for new_row, new_col in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                    if 0 <= new_row < R and 0 <= new_col < C and (new_row, new_col) not in self.seen:
                        self.seen.add((new_row, new_col))
                        q.append((new_row, new_col))
            distance += 1
                
                    
        
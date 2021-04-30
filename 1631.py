# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# starting from (0,0), check the diff among 4 directions, 
# priority queue => current location and max height so far. split out the minimum height curr index
# also another matrix to record the max height on the path
import heapq
class Solution:
    def minimumEffortPath(self, heights):
        R, C = len(heights), len(heights[0])
        memo_matrix = [[float('inf')] * C for _ in range(R)]
        memo_matrix[0][0] = 0
        self.visited = set()

        q = [(0, 0, 0)]
        while q:
            effort, row, col = heapq.heappop(q)
            self.visited.add((row, col)) # We record the node when all its neighbors are visited.
            for new_row, new_col in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if 0 <= new_row < R and 0 <= new_col < C and (new_row, new_col) not in self.visited:
                    new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                    if new_effort < memo_matrix[new_row][new_col]:
                        memo_matrix[new_row][new_col] = new_effort
                        heapq.heappush(q, (new_effort, new_row, new_col))

        
        return memo_matrix[-1][-1] 
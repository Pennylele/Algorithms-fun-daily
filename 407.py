# [[3,3,3,3,3],
#  [3,2,2,2,3],
#  [3,2,1,2,3],
#  [3,2,2,2,3],
#  [3,3,3,3,3]]
# smart solution: 
# 1. process border info into a min-heap
# 2. always pop out the next lowest height and use it to check against its adjacent cells
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        R, C = len(heightMap), len(heightMap[0])
        seen = [[0] * C for _ in range(R)]
        
        hq = []
        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0 or i == R-1 or j == C-1:
                    heapq.heappush(hq, (heightMap[i][j], i, j))
                    seen[i][j] = 1
        
        water = 0
        while hq:
            height, r, c = heapq.heappop(hq)
            for new_r, new_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= new_r < R and 0 <= new_c < C and not seen[new_r][new_c]:
                    seen[new_r][new_c] = 1
                    new_height = heightMap[new_r][new_c]
                    heapq.heappush(hq, (max(new_height, height), new_r, new_c)) # It's important to append the max value of the height, since we want the adjacent cells to compare against the max value of the popped height. The second prob example is a good example to think about it.
                    if height - new_height > 0:
                        water += height - new_height
        
        return water
# # Let's use djistra's algorithm to solve it!
import collections, heapq
# class Solution:
#     def minCost(self, grid):
#         R, C = len(grid), len(grid[0])
#         directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
#         graph = collections.defaultdict(list)
#         # build the graph
#         for i in range(R):
#             for j in range(C):
#                 for d in directions:
#                     weight = (0 if grid[i][j] == d else 1)
#                     new_i = i + directions[d][0]
#                     new_j = j + directions[d][1]
#                     if 0 <= new_i < R and 0 <= new_j < C:
#                         graph[(i, j)].append((new_i, new_j, weight))
    
#         # Djistra's Algorithm
#         pq = [(0, 0, 0)]
        
#         costs = {(i,j): float('inf') for i in range(R) for j in range(C)}
#         costs[(0, 0)] = 0

#         # parents = {(0, 0): None}
#         seen = set()

#         while pq:
#             cost, i, j = heapq.heappop(pq)
#             seen.add((i, j))

#             for new_i, new_j, next_cost in graph[(i, j)]:
#                 new_cost = cost + next_cost
#                 if (new_i, new_j) not in seen and new_cost < costs[(new_i, new_j)]:
#                     heapq.heappush(pq, (new_cost, new_i, new_j))
#                     costs[(new_i, new_j)] = new_cost
#                     #parents[(new_i, new_j)] = (i, j)
#         return costs[(R-1, C-1)]
#////////////////////////O(MN) method///////////////////////////////
# This is actually very smart...
class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        arrow = [(0,1), (0,-1), (1,0), (-1,0)]            
        dp, costs = collections.deque([(0,0,0)]), {}
        
        while dp:
            nx, ny, cost = dp.popleft()
            print(nx, ny, cost)
            while 0 <= nx < m and 0 <= ny < n and (nx, ny) not in costs:
                costs[nx, ny] = cost # following the same directions, the cost is 0
                dp += [(nx+dx, ny+dy, cost+1) for dx, dy in arrow]
                dx, dy = arrow[grid[nx][ny]-1] # following the arrow direction. -1 because of the index diff.
                nx, ny = nx+dx, ny+dy
                print(costs)
                        
        return costs[m-1,n-1] 

s = Solution()
print(s.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
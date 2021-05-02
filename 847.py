# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]

import collections
class Solution:
    def shortestPathLength(self, graph):
        goal = 1 << len(graph) - 1 # e.g. 111 for a graph of length 4
        memo = set()
        q = collections.deque[(i, 0, 1 << i for i in range(len(graph)))]

        # This is a BFS, whenever we meet the goal, we return the step
        while q:
            node, step, state = q.pop()
            if state == goal:
                return step
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append(v, step+1, state | 1 << v) # "|" is OR operation - here we add the v's state to the node's state. 
                    memo.add(state | 1 << v, v)


obj = Solution()
graph = [[1,2,3],[0],[0],[0]]
print(obj.shortestPathLength(graph))
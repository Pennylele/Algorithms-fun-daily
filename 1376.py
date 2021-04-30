import collections, heapq
class Solution:    
    def numOfMinutes(self, n, headID, manager, informTime):
        graph = collections.defaultdict(set)

        for employeeID, manager in enumerate(manager):
            graph[manager].add((informTime[manager], employeeID))

        heap = [(informTime[headID], headID)]
        dist = {}

        while heap:
            time, manager = heapq.heappop(heap)
            if manager in dist:
                continue
            dist[manager] = time
            for informTime, employee in graph[manager]:
                heapq.heappush(heap, (informTime + time, employee))
        return max(dist.values())


s = Solution()
print(s.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
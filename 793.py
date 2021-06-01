# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         hq = []
        
#         def distance(x, y):
#             return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2   
        
#         origin = (0, 0)
#         for p in points:
#             heapq.heappush(hq, (distance(p, origin), p))
        
#         ans = []
#         for _ in range(k):
#             ans.append(heapq.heappop(hq)[1])
        
#         return ans
#///////////////////////////Similar idea, but if we want to do O(nlogk)/////////////////////////////////
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        
        def distance(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2   
        
        origin = (0, 0)
        for p in points:
            if len(hq) < k:
                heapq.heappush(hq, (-distance(p, origin), p)) # we pop out all the big values leaving the k smallest.
            else:
                heapq.heappushpop(hq, (-distance(p, origin), p))
        return [i[1] for i in hq]
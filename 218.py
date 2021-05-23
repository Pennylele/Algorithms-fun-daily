# 1. sort by l and height + r (ending position with height 0)
# 2. Initiate two containers to track the height change, and a heap to provide the largest height so far (to detect the change at l)
# 3. loop through the events, record the height change. We can also safely pop out the prev max height when the l is larger than the height's r.
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for _, r, _ in buildings}))
        
        res = [[0, 0]] # recording the height change
        hq = [(0, float('inf'))] # heap - providing the largest height so far (height, r)
        
        for L, negH, R in events:
            if negH:
                heapq.heappush(hq, (negH, R))
            
            while L >= hq[0][1]:
                heapq.heappop(hq)
            
            if res[-1][1] != -hq[0][0]:
                res.append([L, -hq[0][0]])
        return res[1:]
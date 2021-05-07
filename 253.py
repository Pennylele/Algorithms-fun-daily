# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# I just remembered to mimick how the meeting room should be occupied...
# sorted based on the end time?
# [5, 10],[15, 20], [0, 30]
# priority queue based on ending time
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        pq = [float('-inf')]
        for start, end in sorted(intervals):
            if start >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, end)
        return len(pq)

obj = Solution()
intervals = [[0,30],[5,10],[15,20]]
print(obj.minMeetingRooms(intervals))
            

bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]

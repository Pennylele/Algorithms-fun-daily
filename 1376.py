# Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
# Output: 21
# Actually we can just use a deque and a variable to track the longest time - that probably is faster
import collections
class Solution:    
    def numOfMinutes(self, n, headID, manager, informTime):
        managerMap = collections.defaultdict(list)
        for sub, managerID in enumerate(manager):
            managerMap[managerID].append(sub)
        
        q = collections.deque([(headID, informTime[headID])])
        ans = 0
        while q:
            manager_id, time = q.popleft()
            ans = max(ans, time)
            for sub in managerMap[manager_id]:
                q.append((sub, informTime[sub] + time))
        return ans


s = Solution()
print(s.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
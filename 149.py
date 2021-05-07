# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
import collections

class Solution:
    def maxPoints(self, points):
        def slope(p1, p2):
            if p2[0] - p1[0] == 0: # don't forget to consider the situation when the denomitor is 0
                return float('inf')
            else:
                s = (p2[1] - p1[1]) / (p2[0] - p1[0])
            return s
        
        ans = 0
        for i in points:
            counter = collections.Counter()
            for j in points:
                if i != j:
                    s = slope(i, j) 
                    counter[s] += 1

            if counter:
                ans = max(ans, max(counter.values())+ 1)
            else:
                ans = max(ans, 1)
        return ans

obj = Solution()
points = [[1,1],[2,2],[3,3]]
print(obj.maxPoints(points))


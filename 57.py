# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
class Solution:
    def insert(self, intervals, newInterval):
        left, right = [], []
        MAX = newInterval[1]
        MIN = newInterval[0]
        for l, r in intervals:
            if l > newInterval[1]:
                right.append([l, r])
            elif r < newInterval[0]:
                left.append([l, r])
            else:
                MAX = max(MAX, r)
                MIN = min(MIN, l)
        return left + [[MIN, MAX]] + right

s = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(s.insert(intervals, newInterval))
# Input: arr = [1,0,2,3,4]
# Output: 4
# TEST: arr = [1,0,3,2,4]
class Solution:
    def maxChunksToSorted(self, arr):
        cur_max = float('-inf')
        res = 0

        for i, num in enumerate(arr):
            cur_max = max(cur_max, num)
            if cur_max == i:
                res += 1
        return res


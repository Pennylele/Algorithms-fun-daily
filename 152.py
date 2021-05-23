# nums = [2,3,-2,4,-2]
class Solution:
    def maxProduct(self, nums):
        res, cur_max, cur_min = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            cur_min, cur_max = min(i, cur_min * i, cur_max * i), max(i, cur_min * i, cur_max * i)
            if cur_max > res:
                res = cur_max
        return res
        
obj = Solution()
print(obj.maxProduct([2,3,-2,4,-2]))



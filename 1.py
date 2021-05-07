# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for idx, num in enumerate(nums):
            t = target - num
            if t in d:
                return [d[t], idx]
            d[num] = idx
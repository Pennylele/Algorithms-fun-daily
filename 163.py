class Solution:
    def findMissingRanges(self, nums, lower, upper):
        nums.append(upper + 1)
        
        prev = lower - 1
        res = []
        for i in range(len(nums)):
            if nums[i] - prev == 2:
                res.append(str(nums[i] - 1))
            if nums[i] - prev > 2:
                res.append(str(prev + 1) + "->" + str(nums[i] - 1))
            prev = nums[i]
        return res
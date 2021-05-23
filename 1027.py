class Solution:
    def longestArithSeqLength(self, nums):
        dp = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                dp[(j, nums[j] - nums[i])] = dp.get((i, nums[j] - nums[i]), 1) + 1 # Use an example: [9,4,7,2,10] - 4's max value should be the value of 9's with a diff of -5 plus 1. We are looking backward to see if the previous element has the same diff.
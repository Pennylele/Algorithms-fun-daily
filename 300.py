# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# O(nlogn)
class Solution:
    def lengthOfLIS(self, nums):
        N = len(nums)
        dp = [0] * N
        size = 0, 0

        for i in range(N):
            idx = bisect.bisect_left(dp, nums[i], hi=size)
            dp[idx] = nums[i]
            size = max(size, idx+1)
        return size
# We can also do it in a O(n^2) DP
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp) 
        
        

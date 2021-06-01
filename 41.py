# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
class Solution:
    def firstMissingPositive(self, nums):
        N = len(nums)
        for i in range(N):
            while 0 <= nums[i]-1 < N and nums[nums[i] - 1] != nums[i]: # these 3 lines are important...
                tmp = nums[i] - 1
                nums[tmp], nums[i] = nums[i], nums[tmp]
        
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1

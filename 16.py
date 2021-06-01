# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# This is a two-pointer strategy. Once the first element is set, we do a round of two-pointer algo for the rest of the array
# The result should be kept being updated
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        N = len(nums)

        for i in range(N-2):
            s, e = i + 1, N-1
            while s < e:
                cur = nums[i] + nums[s] + nums[e]
                if cur == target:
                    return cur
                if abs(cur - target) < abs(result - target):
                    result = cur
                if cur < target:
                    s += 1
                if cur > target:
                    e -= 1
        return result
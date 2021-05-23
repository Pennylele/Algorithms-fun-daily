# Can transform it into a sliding window prob
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = 0
        MAX = float('-inf')
        running_sum = 0
        
        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum > target and left <= right: # don't forget left needs to be smaller than right. using while: consider this example [3,2,20,1,1,3] 10
                running_sum -= nums[left]
                left += 1
            if running_sum == target:
                MAX = max(MAX, right - left + 1)
        return len(nums) - MAX if MAX != float('-inf') else -1
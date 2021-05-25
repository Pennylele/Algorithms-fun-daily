# two-pointer
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left, right = 0, len(nums)-1
        idx = len(nums)-1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                bigger = nums[right]
                right -= 1
            else:
                bigger = nums[left]
                left += 1
            ans[idx] = bigger * bigger
            idx -= 1
        return ans
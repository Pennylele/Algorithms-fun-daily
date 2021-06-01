# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# O(n)
# DP problem - at each element, we select whether add it to the MAX or use it by its own
class Solution:
    def maxSubArray(self, nums):
        MAX = float('-inf')

        for i in range(len(nums)):
            nums[i] = max(nums[i], nums[i] + MAX) # have to update nums as well.
            MAX = nums[i] # MAX is a dynamic max recorder. It is always the max for the current index. It start accumulates from the current index onward
        return max(nums)
#////////////////////////////O(nlogn) - ///////////////////////////////
# Kinda want to give up this solution...
# Basically we need to find a middle point to recursively calculate the max value among(best_combined_sum, left_half, right_half). 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)

obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


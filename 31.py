# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]

# Example 4:
# Input: nums = [1]
# Output: [1]
# The replacement must be in place and use only constant extra memory.
# I think the secret is to reverse all the ascending elements from the right, before swapping the first descending num with the first element bigger than it in the following array. 
class Solution:
    def nextPermutation(self, nums):
        def reverse(idx1, idx2):
            while idx1 < idx2:
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
                idx1 += 1
                idx2 -= 1
        
        N = len(nums)
        for i in range(N-1, 0, -1):
            if nums[i] > nums[i-1]:
                reverse(i, N-1)

                x = i
                while x < N:
                    if nums[x] > nums[i-1]:
                        nums[x], nums[i-1] = nums[i-1], nums[x]
                        return nums
                    x += 1        
        
        return nums

obj = Solution()
print(obj.nextPermutation([1,2,3]))
print(obj.nextPermutation([1,2,7,9,8,6,4,1]))
# 1,2,7,1,4,6,8,9

        
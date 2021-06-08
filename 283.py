# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# This method - i in a loop, action when a num != 0
# j is not necessarily pointing to a 0, it always points to the same location as i if nums[i] != 0 initially. But when nums[i] == 0, that's when j stays and wait for the next i where nums[i] != 0 to swap values. So from then on, j will always point to the first 0 in the current operated array.
# It's impossible for j to point to a non-0 element, (after the possibly initial pointers pointing to the same element as i), bc any element that's an 0 would have swapped with j.
class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j], nums[i]
                j += 1
        return nums

# Not very efficient
class Solution:
    def moveZeroes(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    elif nums[j] == 0:
                        j += 1
                i += 1
        return nums

obj = Solution()
print(obj.moveZeroes([0,1,0,3,12]))

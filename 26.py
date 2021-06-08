# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]
# Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1] # we can't swap in this case
                print(nums)
                j += 1
        print(nums)
        return j

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


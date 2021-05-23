# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3, 4]
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1, -1]
# Input: nums = [1], target = 1
# Output: [0, 0]
class Solution:
    def searchRange(self, nums, target):
        def search(left):
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r-l) // 2  #[1] 1 We use len(nums) bc otherwise, we'd get l == r == 0. The returned value would be 0, -1...
                if nums[mid] == target:
                    if target == True:
                        r = mid
                    else:
                        l = mid + 1
                elif nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
        
        l = search(True)
        r = search(False)

        if not len(nums):
            return [-1, -1]
        elif 0 <= l < len(nums) and nums[l] == target: # #[2,2] 3 is the example for why we need 0 <= l < len(nums)
            return [l, r-1] # Here we use r-1 to avoid getting the negative value in a case of [1] 1
        else:
            return [-1, -1]
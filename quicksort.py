import random
class Solution:
    def qs(self, nums):
        def partition(l, r): # return the current index of the randomly selected element.
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            j = l # j to record the first element bigger than the pivot

            for i in range(len(nums)):
                if nums[i] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[j], nums[r] = nums[r], nums[j]
            return j


        def quickSort(l, r):
            if l < r:
                pivotIndex = partition(l, r)

                quickSort(l, pivotIndex - 1)
                quickSort(pivotIndex + 1, r)
        
        n = len(nums)
        quickSort(0, n-1)
        return nums

obj = Solution()
print(obj.qs([10, 7, 8, 9, 1, 5]))
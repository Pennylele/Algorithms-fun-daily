# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# This is a O(nlogn) solution
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
#///////////////////////Quick Sort////////////////////////////////
# Quick Sort should be O(N) on average, since we are only looking at the half of one half and then half of the previous half, etc.
# The worst case is O(N^2) though, if we don't use the random function
class Solution:
    def findKthLargest(self, nums, k):
        def partition(l, r): # return the current index of the randomly selected element.
            pivot = randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            j = l # j to record the first element bigger than the pivot

            for i in range(len(nums)):
                if nums[i] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[j], nums[r] = nums[r], nums[j]
            return j


        def quickSelect(l, r):
            pivotIndex = self.partition(l, r)

            if pivotIndex == n - k:
                return nums[pivotIndex]
            elif pivotIndex > n - k:
                return self.quickSelect(l, pivotIndex-1)
            else:
                return self.quickSelect(pivotIndex+1, r)

        
        n = len(nums)
        return findPivot(0, n-1)

        


obj = Solution()
print(obj.findKthLargest([1,2,2,3,3,4,5,5,6], 4))
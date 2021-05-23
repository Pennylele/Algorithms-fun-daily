# Method of O(nlogn)
# This method is fenwick tree, but it's actually the same idea of bisect's O(n^2). The only optimization we do is to find the idx of the 2*num value in the sorted array. 
# The fenwick records how many elements are smaller than 2*num a head of the current num index.
# Don't forget to add the result to the fenwick tree for processing the next element
# This problem is very similar to the LC315. But the 315 needs to get the rank of the original element and also need to be processed in a reversed way.
class Solution:
    def getSum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & (-i))
        return res
    
    def update(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += (i & (-i))
        
    def reversePairs(self, nums):
        sorted_nums = sorted(nums)
        
        # construct Fenwick tree
        self.tree = [0] * (len(nums) + 1)
        
        ans = 0
        for i, num in enumerate(nums):
            loc = bisect.bisect(sorted_nums, 2*num) # idx is where the 2*num is in the sorted original array => the rank
            idx = self.getSum(loc) # This is to get the current idx of the existing sorted array/or rather how many elements before the current rank. These previous 2 lines of code does the same as the bisect code in the O*(n^2) method
            ans += i - idx
            
            # add the number to the tree
            rank = bisect.bisect_right(sorted_nums, num)
            self.update(rank)
        return ans
            
# ///////////////////////////Method of O(n^2)/////////////////////////////
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        sorted_list = []
        
        for i, num in enumerate(nums):
            idx = bisect.bisect_right(sorted_list, num * 2)
            ans += i - idx # think of this as what its location is in the original array minus its rank in the sorted array. Then the difference is the number of elements bigger than it
            bisect.insort(sorted_list, num)
        return ans
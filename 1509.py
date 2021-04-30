class Solution:
    def minDifference(self, nums: List[int]) -> int:
        small = nsmallest(4, nums)
        large = nlargest(4, nums)
        #print(small, large)
        return min(x-y for x, y in zip(reversed(large), small))
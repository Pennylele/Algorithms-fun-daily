class Solution:
    def longestConsecutive(self, nums):
        memory = set(nums)
        MAX = 1
        for num in nums:
            if num - 1 in nums:
                continue
            counter = 1
            while num + 1 in memory:
                num += 1
                counter += 1
            MAX = max(MAX, counter)
        return MAX

obj = Solution()
print(obj.longestConsecutive([100,4,200,1,3,2]))


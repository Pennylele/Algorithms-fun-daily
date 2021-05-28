class Solution:
    def canPartitionKSubsets(self, nums, k):
        buckets = [0] * k
        if sum(nums) % k != 0:
            return False
        else:
            subsum = sum(nums) // k
        nums.sort(reverse=True)

        def backtrack(start):
            if start == len(nums):
                return True
            for i in range(k):
                buckets[i] += nums[start]
                if buckets[i] <= subsum and backtrack(start+1):
                    return True
                buckets[i] -= nums[start]

                if buckets[i] == 0:
                    return False
            return False
      
        return backtrack(0)

obj = Solution()
print(obj.canPartitionKSubsets([4,3,2,3,5,2,1], 4))


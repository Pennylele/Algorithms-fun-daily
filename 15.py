# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
class Solution:
    def threeSum(self, nums):
        nums.sort()
        N = len(nums)
        res = []
        for i in range(N):
            target = -nums[i]
            if i > 0 and nums[i] == nums[i-1]: # we do this to avoid the repeated patterns
                continue
            # two sum
            if i < N - 1:
                s = i + 1
                e = N - 1
                while s < e:
                    if nums[s] + nums[e] == target:
                        res.append([nums[i], nums[s], nums[e]])
                        while nums[s+1] == nums[s] and s + 1 < e:
                            s += 1 # We do this while loop to avoid the repeated patterns
                        s += 1
                    elif nums[s] + nums[e] > target:
                        e -= 1
                    elif nums[s] + nums[e] < target:
                        s += 1
        return res

obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))

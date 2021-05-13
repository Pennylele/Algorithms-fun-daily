# Let's do this with binary search! It's faster - O(log(sum(nums)) * n)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def getSubGroups(upper):
            count = 0
            cur_sum = 0
            
            for num in nums:
                cur_sum += num
                if cur_sum > upper:
                    count += 1
                    cur_sum = num
            
            return count + 1
        
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            sub_groups = getSubGroups(mid)
            
            if sub_groups > m:
                left = mid + 1
            else:
                right = mid
        
        return right
        
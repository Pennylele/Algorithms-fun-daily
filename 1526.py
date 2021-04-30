class Solution:    
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        ans = 0
        for num in target:
            if num > prev:
                ans += num - prev
            prev = num
        return ans
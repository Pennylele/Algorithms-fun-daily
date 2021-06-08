# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# dp[i] = dp[i-1] + dp[i-2]
class Solution:
    def climbStairs(self, n):
        d = {1: 1, 2: 2}
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]

obj = Solution()
print(obj.climbStairs(5))


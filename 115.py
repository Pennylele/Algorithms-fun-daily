# This is a very typical DP problem and I should get familiar with it.
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        dp = [0] * T
        for i in range(S):
            prev = 1
            for j in range(T):
                old_dpj = dp[j]
                if s[j] == s[i]:
                    dpj += prev
                prev = old_dpj # This works because the old_dpj is equal to the next cell's (i+1, j+1) value
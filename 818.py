# Let's try the DP solution
# The second time I may try the BFS solution, but the BFS takes O(2^n), but DP takes O(nlogn)
class Solution:
    def racecar(self, target: int) -> int:
        dp = [float('inf')] * (target + 1)
        
        for t in range(target+1):
            k = t.bit_length()
            
            if 2**k - 1 == t:
                dp[t] = k
                continue
            
            dp[t] = min(dp[t], k + 1 + dp[2**k - 1 - t])
            
            for j in range(k-1):
                dp[t] = min(dp[t], k - 1 + 1 + j + 1 + dp[t - (2**(k-1) - 2**j)])
        
        return dp[target]
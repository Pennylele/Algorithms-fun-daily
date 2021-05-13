# The dp is dp(i + x, max(m, x))
# dp[i, m] = maximum stones the current player can get from piles[i:] with M=m
# A[i]= total stones of piles[i:]
# when current player pick stones from i to i+x-1
# -> the other player's stones: dp[i+x, max(m, x)]
# -> total stones of current player: A[i] - dp[i+x, max(m, x)]
# we want the current player gets maximum means the other player gets minimum
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        P = len(piles)
        for i in range(P-2, -1, -1):
            piles[i] += piles[i+1]
        
        @lru_cache(None)
        def dp(idx, m):
            if idx + 2 * m > P - 1: 
                return piles[idx]
            return piles[idx] - min(dp(idx + x, max(x, m)) for x in range(1, 2 * m + 1))
                
        return dp(0, 1)
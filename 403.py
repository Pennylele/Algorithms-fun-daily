# Input: stones = [0,1,3,5,6,8,12,17]
# Output: true
class Solution:
    def canCross(self, stones):
        S = len(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for i in range(S):
            stone = stones[i]
            for j in dp[stone]:
                for jump in range(j-1, j+2):
                    new_stone = stone + jump
                    if jump and new_stone in dp:
                        dp[new_stone].add(jump)
        
        return len(dp[stones[-1]]) > 0
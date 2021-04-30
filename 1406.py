# seems important to think of the relations in a minmax game
# Input: values = [1,2,3,-9]
# Output: "Alice"
# dp = [0,0,0,0,0,0,0]
class Solution:
    def stoneGameIII(self, stoneValue):
        V = len(stoneValue)
        dp = [float('-inf')] * V + [0,0,0]

        for i in range(V-1, -1, -1):
            for j in range(1,4):
                dp[i] = max(dp[i], sum(stoneValue[i:i+j]) - dp[i+j])
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

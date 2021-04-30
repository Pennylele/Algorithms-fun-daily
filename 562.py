# Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
# Output: 3
class Solution:
    def longestLine(self, M):
        R, C = len(M), len(M[0])
        dp = [[(0,0,0,0)] * (C + 2) for _ in range(R + 1)]
        ans = 0
        for i in range(1, R+1):
            for j in range(1, C+1):
                if M[i-1][j-1] == 1:
                    dp[i][j] = (dp[i][j-1][0] + 1, dp[i-1][j-1][1] + 1, dp[i-1][j][2] + 1, dp[i-1][j+1][3] + 1)
                    ans = max(ans, max(dp[i][j]))
        return ans


# can check if the 2-digit num is less than or equal to 26
# need also be careful if the 2-digit starts with a 0
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
class Solution:
    def numDecodings(self, s):
        if not s or s[0] == "0": return 0
        S = len(s)
        dp = [0] * (S+1)
        dp[0] = dp[1] = 1

        for i in range(1, S):
            if s[i] != "0":
                dp[i+1] += dp[i]
            if s[i-1] != "0" and s[i-1:i+1] <= 26:
                dp[i+1] += dp[i-1]
        return dp[-1]


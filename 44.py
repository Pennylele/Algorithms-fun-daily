# let's just focus on the DP method right now.
# Input: s = "acdcb", p = "a*c?b"
# Output: false
# can build a table
class Solution:
    def isMatch(self, s, p):
        S, P = len(s), len(p)
        dp = [[False] * (P + 1) for _ in range(S + 1)]
        dp[0][0] = True

        # Fill in the first row for asterik first, bc asterik matches an empty string.
        for i in range(1, P + 1):
            if p[i-1] == "*":
                dp[0][i] = True
            else:
                break
        
        # filling in the rest of the table
        for i in range(1, S+1):
            for j in range(1, P+1):
                if p[j-1] in {s[i-1], "?"}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*": # I think this is the most difficult to understand. I think since * can match a sequence, so either it matches the earlier character or current char mathes the pattern, then * would suffice to make the current char with it a match.
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]



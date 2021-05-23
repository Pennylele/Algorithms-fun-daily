# Naiive way to do it
class Solution:
    def repeatedSubstringPattern(self, s):
        return s in (s+s)[1:-1]
# ///////////////////////////////////
# KMP
# Input: s = "abcabcabcabc"
# Output: true
class Solution:
    def repeatedSubstringPattern(self, s):
        S = len(s)
        dp = [0] * S # index to check for the next ch

        for i in range(1, S):
            j = dp[i-1] # this is the next ch to check against s[i]
            while j > 0 and s[i] != s[j]:
                j = dp[j-1] # this is to try to match the current i with the next possibel match. For example, if s[i] doesn't match dp[i-1], then we check the previous s[i]'s dp value
            if s[i] == s[j]:
                j += 1
            dp[i] = j
        return dp[-1] != 0 and S % (S - dp[-1]) == 0
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Input: s = "cbbd"
# Output: "bb"
# X b a b a d
# b T    
# a   T
# b     T
# a       T
# d         T
class Solution:
    def longestPalindrome(self, s):
        S = len(s)
        dp = [[False] * S for _ in range(S)]
        
        # filling out the diagnols as the base case
        for i in range(S):
            dp[i][i] = True
        
        res = s[:1]
        # filling the right upper half of the matrix
        for col in range(S):
            for row in range(col-1, -1, -1):
                if s[row] == s[col] and ((col - row) < 2 or dp[row+1][col-1] == True):
                    dp[row][col] = True
                    if col - row + 1 > len(res):
                        res = s[row: col+1]
        return res

obj = Solution()
print(obj.longestPalindrome("babad"))
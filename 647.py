# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
class Solution:
    def countSubstrings(self, s):
        S = len(s)
        dp = [[False] * S for _ in range(S)]

        # setting up the diagnol
        for i in range(S):
            dp[i][i] = True
        
        # filling up the rest of the DP table
        count = 0
        for col in range(S): # fix the column
            for row in range(col-1, -1, -1): # moving bottom-up
                if s[row] == s[col] and (col - row <= 1 or dp[row+1][col-1] == True):
                    dp[row][col] = True
                    count += 1
        return count + S

obj = Solution()
print(obj.countSubstrings("aaa"))

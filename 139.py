# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# ////////////////O(n^3)/////////////////////
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True] + [False] * len(s)
        wordDict = set(wordDict)
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and dp[j:i] in wordDict:
                    dp[i] = True # here is dp[i] not dp[j]
                    break # To save some processing time
        return dp[-1]
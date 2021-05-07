# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".
# ////////////////////Using Dynamic Programming/////////////////////////////////////
# Runtime - O(nlogn + nl^2) where n is the # of words and l is the length of a word
# class Solution:
#     def longestStrChain(self, words):
#         # dp data structure - hashmap with key being the word and value being the longest chain.
#         dp = collections.defaultdict(int)
#         MAX = 0
#         # sort the words list, and then starting from the first word building up the chain by updating the dp table (words of the same length won't build up on chain)
#         for word in sorted(words, key=len): # O(nlogn)
#             dp[word] = 1
#             for i in range(len(word)): #O(L=len(word))
#                 test_word = word[:i] + word[i+1:]
#                 if test_word in dp:
#                     dp[word] = max(dp[word], dp[test_word] + 1)
#                     MAX = max(MAX, dp[word])
#         return MAX
#/////////////////////////////DFS + memo/////////////////////////////////
class Solution:
    def longestStrChain(self, words):

        def dfs(word, s, memo):
            if word in memo: return memo[word]
            count = 0
            for i in range(len(word)):
                test_word = word[:i] + word[i+1:]
                if test_word in s:
                    count = max(count, dfs(test_word, s, memo))
            memo[word] = count + 1
            return memo[word]
 
        s = set(words)
        MAX = 0
        for word in s:
            MAX = max(MAX, dfs(word, s, {}))
        return MAX

obj = Solution()
words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
print(obj.longestStrChain(words))
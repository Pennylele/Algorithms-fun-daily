# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
class Solution:
    def lengthOfLongestSubstring(self, s):
        d = {}
        start = 0
        MAX = 0

        for idx, char in enumerate(s):
            if char in d:
                MAX = max(MAX, idx - start)
                start = max(d[char] + 1, start)
            d[char] = idx
        return MAX

obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
print(obj.lengthOfLongestSubstring("abba"))
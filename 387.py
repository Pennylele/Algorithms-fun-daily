# Input: s = "loveleetcode"
# Output: 2
class Solution:
    def firstUniqChar(self, s):
        counter = collections.Counter(s)

        for idx, ch in enumerate(s): # istead of looping through the counter, we loop through the string
            if counter[ch] == 1:
                return idx
        return -1
        
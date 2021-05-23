class Solution:
    def checkRecord(self, s: str) -> bool:
        count = collections.Counter()
        for idx, ch in enumerate(s):
            count[ch] += 1
            if ch == 'A' and count[ch] == 2:
                return False
            if idx > 2 and s[idx-1] == s[idx-2] == ch == 'L':
                return False
        return True
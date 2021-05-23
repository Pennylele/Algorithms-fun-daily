class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        if len(s) == 1 and s[0] == "?": return "a"
        for i in range(len(s)):
            if s[i] == "?":
                for x in "abc":
                    if i > 0 and i < len(s) - 1 and s[i-1] != x and s[i+1] != x:
                        s[i] = x
                    elif i == 0 and s[i+1] != x:
                        s[i] = x
                    elif i == len(s)-1 and s[i-1] != x:
                        s[i] = x
        return s
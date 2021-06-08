# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
class Solution:
    def romanToInt(self, s):
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
        if not s: return 0
        total = roman[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total

obj = Solution()
print(obj.romanToInt("MCMXCIV"))
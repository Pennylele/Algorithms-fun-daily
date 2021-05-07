# We need at least one extra char to convert str1 to str2. So str2 can't have all 26 chars.
class Solution:
    def canConvert(self, str1, str2):
        if str1 == str2: return True
        # check whether one char maps to 2 different chars
        d = {}
        for i in range(len(str1)):
            if str1[i] not in d:
                d[str1[i]] = str2[i]
            elif str1[i] in d and d[str1[i]] != str2[i]:
                return False

        # Then check if all 26 chars are present in str2
        return len(set(str2)) < 26

obj = Solution()
print(obj.canConvert("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))
print(obj.canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))

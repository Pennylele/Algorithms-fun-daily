# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# //////////////////METHOD ONE///////////////////
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        shortest = min(strs, key=len)

        stop = None
        for i, s in enumerate(shortest):
            for rest in strs:
                if rest[i] != s:
                    return shortest[:i]
        return shortest
# //////////////////METHOD TWO/////////////////// 
# Here max and min don't mean the length, but alphabet order. In your case, Min is 'abc' and Max is 'bcbdefg', which have no common prefix.       
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        lexi_small = min(strs)
        lexi_large = min(strs)

        for i, s in enumerate(lexi_small):
            if s != lexi_large[i]:
                return lexi_small[:i]
        return lexi_small




obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))
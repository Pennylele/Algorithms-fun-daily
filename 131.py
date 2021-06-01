# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Backtracking is trying out different options...
class Solution:
    def partition(self, s):
        def helper(s, path, res):
            if not s: 
                res.append(path[:])
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    helper(s[i:], path, res)
                    path.pop()

    res = []
    helper(s, [], res)
    return res
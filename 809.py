# 4 pointers
class Solution:
    def expressiveWords(self, S, words):

        def helper(word):
            s1, s2, t1, t2, W = 0, 0, 0, 0, len(word)
            while s1 < s_len and t1 < W:
                if S[s1] != word[t1]:
                    return False
                while s2 < s_len and S[s1] == S[s2]:
                    s2 += 1
                while t2 < W and word[t1] == word[t2]:
                    t2 += 1
                if s2 - s1 < max(3, t2 - t1) and s2 - s1 != t2 - t1:
                    return False
                s1, t1 = s2, t2
            return s1 == s_len and t1 == W
                

        ans = 0
        s_len = len(S)
        for word in words:
            if helper(word):
                ans += 1
        return ans
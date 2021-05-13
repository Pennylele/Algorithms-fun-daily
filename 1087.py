class Solution:
    def expand(self, S):
        ans = []

        def backTrack(idx, word):
            if idx == len(S):
                ans.append(word)
                return
            
            x = S[idx]
            if x == "{":
                end = S.index("}", idx) # '}' after the idx-th index is searched
                options = S[idx+1: end].split(',')

                for option in sorted(options):
                    backTrack(end + 1, word + option)
            else:
                backTrack(idx+1, word + x)

        
        backTrack(0, "")
        return ans
# S = "abcdebdde", T = "bde"
#       a b c d e b d d e
#--------------------------
#    0  0 0 0 0 0 0 0 0 0    
# b inf i 1 2 3 4 1 2 3 4
# d inf i i i 3 4 1 2 3 4
# e inf i i i i 4 5 6 7 4

class Solution:
    def minWindow(self, S, T):
        s_len = len(S)
        t_len = len(T)

        dp = [[0] * (s_len + 1) for _ in range(t_len + 1)]

        for i in range(1, t_len+1):
            dp[i][0] = float('inf')
        
        # populate the dp table
        for i in range(1, t_len + 1):
            for j in range(1, s_len + 1):
                if T[i-1] == S[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1] + 1
                    
        
        # loop through the last row of the dp table for the smallest length
        min_len = float('inf')
        end_idx = 0
        for i in range(s_len+1):
            if dp[t_len][i] < min_len:
                min_len = dp[t_len][i]
                end_idx = i
        
        if min_len == float('inf'): return ""
        
        return S[end_idx - min_len: end_idx]
        

        

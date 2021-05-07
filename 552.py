# IF we don't consider A at the moment. Just look at P and L.
# I think this problem is really difficult to think of:
# dp[i]the number of all possible attendance (without 'A') records with length i :

# end with "P": dp[i-1]
# end with "PL": dp[i-2]
# end with "PLL": dp[i-3]
# end with "LLL": is not allowed
# so dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
class Solution:
    def checkRecord(self, n):
        if n == 0: return 0
        if n == 3: return 3
        # calculate the combinations without "A"
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 2, 4

        for i in range(3, n+1):
            dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % modulo
        
        res = dp[n]

        # Then we add the "A" to the combinations
        for i in range(1, n+1):
            res += dp[i-1] * dp[n-i] # really diffiult to make sense of, but gonna let it go. Below is some thoughts:
        return res % modulo

# This formula is to add "A" in different positions inside the string of length n. For example, if n = 4, res += dp[0] * dp[3] + dp[1] * dp[2] + dp[2] * dp[1] + dp[3] * dp[0] which corresponds to adding "A" to position 0,1,2,3, so adding the combinations of dp[0] * dp[3], dp[1] * dp[2], etc could give us all the combinations with "A".
# PL without "A"
# n = 1 => 
# n = 2 => P, L
# n = 3 => PP, PL, LL, LP
# n = 4 => PPP, PLL, PLP, LLP, LPL, PPL, LPP  
# Can try to place A in different index positions to validate if the line of code is valid. 


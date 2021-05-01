# It's important to understand how we calculate the probability of N
# dp[n] = 1/W * (dp[n-1] + dp[n-2] + dp[n-3] + ...)
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0] * (N+1)
        dp[0] = 1 # because if not picking anything, the probability of getting N or less points is 100%
        running_sum = 0 # This records all the probabilities before the current i (target point). This running_sum should cover dp[i] from 
        
        for i in range(1, N+1):
            if i - 1 < K: # we are checking this because from K to N, we won't be able to pick a card anymore
                running_sum += dp[i - 1]
            if i - 1 - W >= 0: # when i (current value within N) is greater than the W (options), we have reached end of our search, so the rest would be removing the probabilities.
                running_sum -= dp[i - 1 - W]
                
            dp[i] = 1 / W * running_sum
        return sum(dp[K:N+1])
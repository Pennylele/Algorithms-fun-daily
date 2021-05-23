# burst the smaller values; burst smaller values in between 2 other numbers.
# Then another interesting idea come up. Which is quite often seen in dp problem analysis. That is reverse thinking. Like I said the coins you get for a balloon does not depend on the balloons already burst. Therefore
# instead of divide the problem by the first balloon to burst, we divide the problem by the last balloon to burst.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        for left in range(n-2, 0, -1):
            for right in range(left, n-1):
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], nums[k] * nums[left-1] * nums[right+1] + dp[left][k-1] + dp[k+1][right])
                    print(dp)
        return dp[1][n-2]
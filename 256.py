# Since we only have 3 rows, we can just write them out specifically
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1: return min(costs[0])
        rows = len(costs)
        dp = costs[0]
        for i in range(1, rows):
            prev = dp[:]
            dp[0] = costs[i][0] + min(prev[1:3])
            dp[1] = costs[i][1] + min(prev[0], prev[2])
            dp[2] = costs[i][2] + min(prev[:2])

        return min(dp)
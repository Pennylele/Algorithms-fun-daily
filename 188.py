class Solution:
    def maxProfit(self, K: int, prices: List[int]) -> int:
        if not prices: return 0
        P = len(prices)
        buy = [[0] * (K+1) for _ in range(P)]
        sell = [[0] * (K+1) for _ in range(P)]
        
        ans = 0
        if K > P//2:
            for i in range(1, P):
                if prices[i] - prices[i-1] > 0:
                    ans += prices[i] - prices[i-1] 
            return ans
        
        for k in range(1, K+1):
            buy[0][k] -= prices[0]
        
        for i in range(1, P):
            for k in range(1, K+1):
                buy[i][k] = max(buy[i-1][k], sell[i-1][k-1] - prices[i])
                sell[i][k] = max(sell[i-1][k], buy[i-1][k] + prices[i])
        return max(sell[-1])
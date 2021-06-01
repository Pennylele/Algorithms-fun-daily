# buy[i] and sell[i] as 2 DP arrays
# buy[i][k] ith day the last action is BUY and we have done K transactions.
class Solution:
    def maxProfit(self, K, prices):
        if not prices: return 0
        P = len(prices)
        buy = [[0] * (K+1) for _ in range(P)]
        sell = [[0] * (K+1) for _ in range(P)]
        
        ans = 0
        if K > P//2: # This means that there's no limit of how many transactions we can use. 
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
                print(buy)
        return max(sell[-1])

obj = Solution()
print(obj.maxProfit(2, [3,2,6,5,0,3]))

# [[0, -3, -3], [0, -2, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, -3, -3], [0, -2, -2], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# [[0, -3, -3], [0, -2, -2], [0, -2, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, -3, -3], [0, -2, -2], [0, -2, -2], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# [[0, -3, -3], [0, -2, -2], [0, -2, -2], [0, -2, 0], [0, 0, 0], [0, 0, 0]]
# [[0, -3, -3], [0, -2, -2], [0, -2, -2], [0, -2, -1], [0, 0, 0], [0, 0, 0]]
# it's a bit difficult to keep track of it. But -1 for exmaple, comes from -2 + 6 - 5 (we buy on the day of price 5)

# [[0, -3, -3], [0, -2, -2], [0, -2, -2], [0, -2, -1], [0, 0, 0], [0, 0, 0]]
# [[0, -3, -3], [0, -2, -2], [0, -2, -2], [0, -2, -1], [0, 0, 4], [0, 0, 0]]

# [[0, -3, -3], [0, -2, -2], [0, -2, -2], [0, -2, -1], [0, 0, 4], [0, 0, 0]]
# [[0, -3, -3], [0, -2, -2], [0, -2, -2], [0, -2, -1], [0, 0, 4], [0, 0, 4]]
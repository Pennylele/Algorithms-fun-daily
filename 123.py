# Traditional DP method
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case
        N = len(prices)
        if N == 0: return 0
        
        # create the buy and sell 2D DP arrays
        buy = [[0] * 3 for _ in range(N)]
        sell = [[0] * 3 for _ in range(N)]
        
        # main DP transition function
        buy[0][1], buy[0][2] = -prices[0], -prices[0]
        
        for i in range(1, N): # i is the ith day
            for j in range(1, 3): # j is the transaction times
                buy[i][j] = max(buy[i-1][j], sell[i-1][j-1] - prices[i])
                sell[i][j] = max(sell[i-1][j], buy[i-1][j] + prices[i]) # we use j bc sell completes the j's transaction with the buy.
        return max(sell[-1])
# A weird method
# [1,2,4,2,5]
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)
            #print(t1_cost, t1_profit, t2_cost, t2_profit)

        return t2_profit
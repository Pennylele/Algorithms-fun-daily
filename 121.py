# Input: prices = [7,1,5,3,6,4]
# Output: 5
class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        minPri = prices[0], maxPri = 0
        for i in range(1, len(prices)):
            minPri = min(minPri, prices[i])
            maxPri = max(maxPri, prices[i] - minPri)
        return maxPri

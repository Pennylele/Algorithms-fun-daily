# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# 1,4,9
# Time complexity - O(n^(2/h​)) - BFS on an n-ary tree
class Solution:
    def numSquares(self, n):
        # find all the possible unique squares that could make up to n
        squares = [i**2 for i in range(int(n ** 0.5) + 1)]
        
        # BFS
        step = 1 # important - setting it to 1. Think of example of 36
        q = {n}
        while n:
            new_q = set()
            for i in q:
                for j in squares:
                     if j - i == 0:
                        return step
                    new_q.add(j - i)
            q = new_q
            step += 1
            new_q = set()
#/////////////////////////The DP solution is great////////////////////////////////
class Solution:
    def numSquares(self, n):
        dp = [0] + [float('inf')] * n

        for i in range(1, n+1):
            for j in range(1, int(n ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[n]

obj = Solution()
print(obj.numSquares(12))
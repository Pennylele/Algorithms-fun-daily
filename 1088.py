# Input: 20
# Output: 6
# Explanation: 
# The confusing numbers are [6,9,10,16,18,19].
# 6 converts to 9.
# 9 converts to 6.
# 10 converts to 01 which is just 1.
# 16 converts to 91.
# 18 converts to 81.
# 19 converts to 61.
class Solution:
    def confusingNumberII(self, N):
        d = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.ans = 0

        def dfs(num, rotation, digit):
            if num != rotation:
                self.ans += 1
            for i in d:
                if num == 0 and i == 0:
                    continue
                if num * 10 + i <= N:
                    dfs(num * 10 + i, d[i] * digit + rotation, digit * 10)


        dfs(0, 0, 1)
        return self.ans

# I think I understand the math now.
# Assume i < j, there are four possible expression:
# |x[i] - x[j]| + |y[i] - y[j]| = (x[i] - x[j]) + (y[i] - y[j]) = (x[i] + y[i]) - (x[j] + y[j])
# |x[i] - x[j]| + |y[i] - y[j]| = (x[i] - x[j]) - (y[i] - y[j]) = (x[i] - y[i]) - (x[j] - y[j])
# |x[i] - x[j]| + |y[i] - y[j]| = -(x[i] - x[j]) + (y[i] - y[j]) = (-x[i] + y[i]) - (-x[j] + y[j])
# |x[i] - x[j]| + |y[i] - y[j]| = -(x[i] - x[j]) - (y[i] - y[j]) = (-x[i] - y[i]) - (-x[j] - y[j])

# So we can see, the expression
# |x[i] - x[j]| + |y[i] - y[j]| + |i - j| = f(j) - f(i)

# where f(i) = p * x[i] + q * y[i] + i
# with p = 1 or -1, q = 1 or -1
# But I've never heard the manhattan distance...
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res, n = 0, len(arr1)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            smallest = p * arr1[0] + q * arr2[0] + 0
            for i in range(n):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(res, cur - smallest)
                smallest = min(smallest, cur)
        return res
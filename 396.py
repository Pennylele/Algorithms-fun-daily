#   f(i)          = 0 * A[0] + 1 * A[1] + 2 * A[2] + .... +  (k-1) * A[k-1] + k * A[k]
#   f(i+1)        = 1 * A[0] + 2 * A[1] + 3 * A[2] + ...  +     k  * A[k-1] + 0 * A[k] 
# =>f(i+1) - f(i) =     A[0]   +   A[1]   +   A[2] + ...  +       A[k-1]    - k * A[k] 
#    = (A[0]   +   A[1]   +   A[2] + ...  +       A[k-1] +  A[k]) - (k+1) * A[k]
#    = sum(Array) - A[k] * array.length
# => f(i+1) = f(i) + sum(Array) -  last element * array.length
class Solution:
    def maxRotateFunction(self, nums):
        MAX = curr = sum(i * j for i, j in enumerate(nums))
        s = sum(nums)
        k = len(nums)

        while nums:
            curr += s - nums.pop() * k
            MAX = max(MAX, curr)
        return MAX



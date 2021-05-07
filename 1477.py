# Dynamic Programming, Sliding Window
# There is a dp array that tracks the min length of the subarray that sums up to target
# Then in the sliding window, we are tracking the sum and the length of the current subarray that sums up to target.
class Solution:
    def minSumOfLengths(self, arr, target):
        A = len(arr)
        dp = [float(inf)] * A

        left, window, res = 0, 0, float('inf')
        for right in range(A):
            window += arr[right]
            while window > target:
                window -= arr[left]
                left += 1
            if window == target:
                cur_window = right - left + 1
                res = min(res, cur_window + dp[left-1])
                dp[right] = min(dp[left-1], cur_window)
            else:
                dp[right] = dp[right-1]
        return res if res != float('inf') else -1 
                

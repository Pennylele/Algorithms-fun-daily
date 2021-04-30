import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], x[-1]))
        dp = [0] * len(envelopes)
        size = 0
        for w, h in envelopes:
            idx = bisect.bisect_left(dp, h, hi=size)
            dp[idx] = h
            size = max(size, idx+1)
        return size

s = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(s.maxEnvelopes(envelopes)) # output = 3
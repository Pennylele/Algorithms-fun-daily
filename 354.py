# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: x[0], -x[1]) # [[2,3],[5,4],[6,7],[6,4]]
        # We need to sort the second value negatively because we want to avoid having 2 envelopes share the same width (e.g.) being fit together. Example edge case: [[4,5],[4,6],[6,7],[2,3],[1,1]] => sorted: [[1, 1], [2, 3], [4, 5], [4, 6], [6, 7]]

        E = len(envelopes)
        lst = [0] * E

        size = 0
        for w, h in envelopes:
            idx = bisect.bisect_left(lst, h, hi=size)
            lst[idx] = h
            size = max(size, idx + 1)
        return size

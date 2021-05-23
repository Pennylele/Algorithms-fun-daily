# This problem is a hard ask, until you realize that we've actually solved this problem before in other sliding window problems. Generally, the sliding window problems have some kind of aggregate, atMost k, largest substring, min substring with k etc. They're always "given an array or string, find some computed sub problem" value.

# So how do we use this our advantage? Well, the ask: different integers in that subarray is exactly K is exactly this. We can rewrite the problem to something like this:

# subArrayExactlyK = subArrayAtMostK - subArrayAtMostK - 1. This is basically saying, give me the amount of subarrays we can form with at least 3, and give me the amount of subarrays we can form with at least 2, and the diff between the two will be only subarrays at 3 (since we have eliminated everything 2 and under).

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K-1)
    
    def atMostK(self, A, K):
        left = 0
        counter = collections.Counter()
        res = 0
        for right, num in enumerate(A):
            if counter[num] == 0:
                K -= 1
            counter[num] += 1
            while K < 0:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    K += 1
                left += 1
            res += right - left + 1
        return res 

            
class Solution:
    def kthSmallest(self, matrix, k):
        res = []
        for i in matrix:
            res += i

        heapq.heapify(res)
        for i in range(k):
            x = heapq.heappop(hq)
        return x


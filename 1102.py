class Solution:
    def maximumMinimumPath(self, A):
        hq = [(-A[0][0], 0, 0)]
        R, C = len(A), len(A[0])

        visited = {(0, 0)}
        while hq:
            value, r, c = heapq.heappop(hq)
            if r == R - 1 and c == C - 1:
                return -value
            for new_r, new_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= new_r < R and 0 <= new_c < C and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    heapq.heappush(hq, (max(-A[new_r][new_c], value), new_r, new_c))
        return -1
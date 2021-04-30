# yi + yj + |xi - xj| = yi - xi + yj + xj 
# Find max value from 2 things - yi - xi and yj + xj. And the constraint is xj - xi <= k
# If we use a monitonic deque
import collections
class Solution:
    def findMaxValueOfEquation(self, points, k):
        q = collections.deque()
        res = float('-inf')

        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            res = max(res, q[0][0] + x + y)
            while q and y-x > q[-1][0]: # making sure that the first element in the deck should be the largest y - x
                q.pop()
            q.append((y-x), x)
        return res


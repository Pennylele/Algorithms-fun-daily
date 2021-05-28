# Both the Time Complexity and space complexity for BFS are: O((max⁡(∣x∣,∣y∣)^2))
# 8 directions - if (r, c), then (r-2, c+1), (r-2, c-1), (r-1, c+2), (r-1, c-2), (r+1, c+2), (r+1, c-2), (r+2, c+1), (r+2, c-1)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque([(0, 0, 0)])
        seen = set()
        while q:
            r, c, step = q.popleft()
            if r == x and c == y:
                return step
            for new_r, new_c in (r-2, c+1), (r-2, c-1), (r-1, c+2), (r-1, c-2), (r+1, c+2), (r+1, c-2), (r+2, c+1), (r+2, c-1):
                if (new_r, new_c) not in seen:
                    seen.add((new_r, new_c))
                    q.append((new_r, new_c, step+1))
#//////////////////////////Optimization///////////////////////////////////
# The coordinates are symmetrical, so we can just focus on 1 out of 4 total quadrants.
# Also, the neighbor cells can be reached by 2 jumps, so we can simply limit the boundary between -2 to x+2
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque([(0, 0, 0)])
        seen = set()
        x = abs(x)
        y = abs(y)

        while q:
            r, c, step = q.popleft()
            if r == x and c == y:
                return step
            for new_r, new_c in (r-2, c+1), (r-2, c-1), (r-1, c+2), (r-1, c-2), (r+1, c+2), (r+1, c-2), (r+2, c+1), (r+2, c-1):
                if (new_r, new_c) not in seen and -2 <= new_r < x + 2 and -2 <= new_c < y + 2:
                    seen.add((new_r, new_c))
                    q.append((new_r, new_c, step+1))
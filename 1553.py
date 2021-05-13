import collections
# BFS method is easier to think of.
class Solution:
    def minDays(self, n):
        q = collections.deque(n)
        seen = set()
        days = 0
        while q:
            for _ in range(len(q)):
                oranges = q.popleft()
                if oranges == 0:
                    return days
                
                if oranges % 3 == 0 and oranges // 3 not in seen:
                    cur = oranges // 3
                    seen.add(cur)
                    q.append(cur)
                
                if oranges % 2 == 0 and oranges // 2 not in seen:
                    cur = oranges // 2
                    seen.add(cur)
                    q.append(cur)

                if oranges - 1 not in seen:
                    cur = oranges - 1
                    seen.add(cur)
                    q.append(cur)

            days += 1

#////////////////////The DP method is kinda tough////////////////////////////
# Great top-down DP template
class Solution:
    def minDays(self, n: int) -> int:
        self.memo = {}
        
        def dp(n):
            if n in self.memo:
                return self.memo[n]
            
            if n == 0: return 0
            if n == 1: return 1
            
            ans = 1 + min(n%3 + dp(n//3), n%2 + dp(n//2))
                          
            self.memo[n] = ans
            
            return ans
        
        return dp(n)
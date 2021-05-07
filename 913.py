# Wondering why the method is O(n^3)...
# I think probably because for each node, it could have all the other nodes as its neighbors, so that's n^2, and then for each move, we do a round of dfs, so it's almost O(n^3).
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(m, c, moves):
            if moves > len(graph) * 2:
                return 0
            if m == c:
                return 2
            if m == 0:
                return 1
            
            # mouse turn
            if moves % 2 == 0:
                canDraw = False
                for nei in graph[m]:
                    ans = dp(nei, c, moves+1)
                    if ans == 1:
                        return 1
                    if ans == 0:
                        canDraw = True
                
                if canDraw == True:
                    return 0
                else:
                    return 2
            # cat turn
            else:
                canDraw = False
                for nei in graph[c]:
                    if nei == 0:
                        continue
                    ans = dp(m, nei, moves+1)
                    if ans == 2:
                        return 2
                    if ans == 0:
                        canDraw = True
                
                if canDraw == True:
                    return 0
                else:
                    return 1
            
        return dp(1, 2, 0)
# Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]
# Output: [0,2,4,2]
dp records the edit distance
#---------DP table setup----------
# [[4, 4, 4, 4, 4], 
#  [4, 4, 4, 4, 4], 
#  [4, 4, 4, 4, 4], 
#  [4, 4, 4, 4, 4]]
#---------DP table-------------
#---------DP table result---------
# [[4, 4, 4, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 4, 4, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 4, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 4, 4, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 4, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 3, 4, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 3, 3, 4], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 3, 3, 1], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 3, 3, 1], [4, 4, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 3, 3, 1], [4, 2, 4, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 3, 3, 1], [4, 2, 1, 4, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 3, 3, 1], [4, 2, 1, 2, 4]]
# [[False, True, True, True, True], [2, 2, 1, 0, 2], [1, 1, 3, 3, 1], [4, 2, 1, 2, 2]]
#---------DP table-------------
# Parents: [[0, 0, 0, 0, 0], [2, 2, 0, 0, 1], [3, 3, 0, 0, 2], [2, 4, 0, 0, 1]]
# Idea

# Let's first calculate the minimum edit distance without worrying about the path. We can use 2D DP to do that:

#     dp[i][v] means the minimum edit distance for tp[:i+1] ending with city v.

# The trainsition function is:

#     dp[i][v] = min(dp[i-1][u] + edit_cost(v)) for all edges (u, v)

# , where edit_cost(v) at index i is names[v] != tp[i].

# And the minimum edit distance will be min(dp[-1][v] for v in range(n)).

# To construct the optimal path, we can maintain a 2D array (or dict) prev when populate dp. Suppose prev[i][v] is u. Then (u, v) is the ending edge of the optimal path at dp[i][v].


# Complexity

# Time complexity: O(N^2 * len(tp))
# Space complexity: O(N * len(tp))


class Solution:
    def mostSimilar(self, n, roads, names, targetPath):
        # n is the # of cities
        # roads are the open
        # names are the city names based on their numerical representation
        # targetPath is the path we are benchmarking.
        #-------------------------------------------------
        # Building the graph
        graph = collections.defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        # Setting up the DP and populating data into it, as well as their parent path
        ## DP's row length is set as length of the target path; col as the number of cities
        m = len(targetPath)
        dp = [[float('inf')] * n for _ in range(m)]
        parents = [[0] * n for _ in range(m)]
        
        ## Find the starting point
        for i in range(n):
            dp[0][i] = 0 if names[i] == targetPath[0] else 1
        
        ## Implement the transition function
        for i in range(1, m):
            for v in range(n):
                for u in graph[v]:
                    if dp[i-1][u] < dp[i][v]: # finding the min dp[i][v]
                        dp[i][v] = dp[i-1][u]
                        parents[i][v] = u
                dp[i][v] += (names[v] != targetPath[i])
        
        # re-construct the path
        ## Find the end node
        path = [0]
        min_dist = float('inf')
        for i in range(n):
            if dp[-1][i] < min_dist:
                min_dist = dp[-1][i]
                path[0] = i
        
        ## bottom-up the parent trail
        for i in range(m-1, 0, -1): # Please notice that we want the path to end at 1st row...
            p = parents[i][path[-1]]
            path.append(p)
        return path[::-1]

            



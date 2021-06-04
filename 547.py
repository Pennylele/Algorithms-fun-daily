# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# My initial code, time complexity - O(n^2) where n is the row and col of the matrix.
class Solution:
    def findCircleNum(self, M):
        # build the graph
        n = len(M)
        graph = {k: [] for k in range(1, n+1)}
        
        for idx, lst in enumerate(M):
            for i in range(len(lst)):
                if lst[i] == 1:
                    graph[idx+1].append(i+1) # {1: [1, 2], 2: [1, 2], 3: [3]}
        
        # dfs method
        def dfs(node):
            for nei in graph[node]:
                if nei not in self.visited:
                    self.visited.add(nei)
                    dfs(nei)

        # DFS to find how many components based on the number of DFS calls
        ans = 0
        self.visited = set()
        for i in range(1, n+1):
            if i not in self.visited:
                self.visited.add(i)
                dfs(i)
                ans += 1
        return ans
#///////////////////////Cleaner DFS//////////////////////////////
class Solution:
    def findCircleNum(self, M):
        def dfs(node):
            for nei, isConnect in enumerate(M[node]):
                if isConnect and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        n = len(M)
        ans = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans
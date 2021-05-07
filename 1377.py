class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # dfs
        def dfs(node, time, prob):
            neighbors = graph[node]
            unvisited = [nei for nei in neighbors if nei not in self.visited]
            
            if time > t:
                return
            
            if node == target:
                if time == t or not unvisited: # meaning we have reached to the leaves
                    self.ans = prob
                return
            
            if unvisited:
                p = 1/len(unvisited)
                
            for nei in unvisited:
                self.visited.add(nei)
                dfs(nei, time+1, prob * p)
                self.visited.remove(nei)
            
        
        # create an adjacency list (graph)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # start dfs
        self.ans = 0
        self.visited = {1}
        dfs(1, 0, 1)
        return self.ans
class Solution:
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        for idx, char in enumerate(equations):
            graph[char[0]][char[1]] = values[idx]
            graph[char[1]][char[0]] = 1/values[idx] 
        
        def dfs(x, y, multiply):i >
            if x == y: return multiply
            for nei in graph[x]:
                if nei not in seen:
                    seen.add(nei)
                    res = dfs(nei, y, graph[x][nei] * multiply)
                    if res != -1: return res
            return -1

        ans = []
        for x, y in queries:
            if x not in graph or y not in graph:
                ans.append(-1)
            else:
                seen = set()
                ans.append(dfs(x, y, 1))
        return ans
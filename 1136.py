# detect cycle - return -1
# If not, we can use DFS to find the longest path.
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # create the graph
        #graph = collections.defaultdict(list) # can't use this, as explained in the later code
        graph = {i: [] for i in range(1, n+1)}
        for u, v in relations:
            graph[u].append(v)
        
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            else:
                visited[node] = -1
            
            max_len = 1
            for nei in graph[node]: #a new dictionary entry is added when checking self.graph[node] it creates a new value in the default dictionary if such value did not exist.
                length = dfs(nei)
                if length == -1:
                    return -1
                else:
                    max_len = max(length + 1, max_len)
            # mark as visited
            visited[node] = max_len
            return max_len
        
        
        max_length = -1
        for node in graph.keys():
            length = dfs(node)
            # we meet a cycle!
            if length == -1:
                return -1
            else:
                max_length = max(length, max_length)
        return max_length
#//////////////////////////Topological Sort/////////////////////////////////////
class Solution:
    def minimumSemesters(self, n, relations):
        # create the indegrees and outdegrees
        outdegrees = collections.defaultdict(list)
        indegrees = {i: 0 for i in range(1, n+1)}
        
        for u, v in relations:
            outdegrees[u].append(v)
            indegrees[v] += 1
        
        # find the node that doesn't have another node coming in
        queue = collections.deque([i for i in indegrees if indegrees[i] == 0])
        
        # start counting
        ans = 0
        courses_taken = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                courses_taken += 1
                for nei in outdegrees[node]:
                    indegrees[nei] -= 1
                    if indegrees[nei] == 0:
                        queue.append(nei)
        return ans if courses_taken == n else -1
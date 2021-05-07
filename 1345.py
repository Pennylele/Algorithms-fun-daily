class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = collections.defaultdict(list)
        for idx, num in enumerate(arr):
            graph[num].append(idx)
            
        q = collections.deque([0])
        visited = set()
        ans = 0
        A = len(arr)
        while q:
            for _ in range(len(q)): # very important - I'm kinda surprised by using len(q) as the range since the q value is changing.
                node = q.popleft()
                
                if node == A - 1:
                    return ans
                
                NEXT = []
                if node > 0:
                    NEXT.append(node - 1)
                if node < A-1:
                    NEXT.append(node + 1)
                if arr[node] in graph:
                    NEXT.extend(graph[arr[node]])
                    del graph[arr[node]] # to delete is to avoid the situation when we have [7,7,7,7,7,7,7,7,...] kind of situation
                
                for nei in NEXT:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            ans += 1
            
            
            
        
        
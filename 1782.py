class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # create a grpah counting degrees for each node, as well as the edge count
        degrees = [0] * (n+1) # because nodes is 1-based
        edgeCounts = collections.defaultdict(int)
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
        
            if u > v:
                u, v = v, u # preparing for edge counts => this problem is interesting in that it's an uncirected graph, we we do need to count the repeated edges...

            edgeCounts[(u, v)] += 1
        
        # Don't forget to sort the degrees
        sortedDegrees = sorted(degrees[1:])
        
        # Use 2 pointers to calculate the count (potential candidate: without worrying about removing the edges between the 2 nodes)  
        ans = []
        for val in queries: # need to do each round of query value
            cnt = 0
            r = n-1
            for l in range(n-1): # 1. need to add to the cnt for each node. 2. we use n-1 as the range bc we need to calculate a pair of node's edge counts that satisfy the val requirement
                while l < r and sortedDegrees[l] + sortedDegrees[r] > val:
                    r -= 1
                
                if r > l:
                    cnt += n - 1 - r
                else:
                    cnt += n - l - 1
                            
            # Removing the invalid pairs (updating the count)
            for u, v in edgeCounts:
                if degrees[u] + degrees[v] > val and degrees[u] + degrees[v] - edgeCounts[(u,v)] <= val:
                    cnt -= 1
            ans.append(cnt)
        return ans
        
        
        
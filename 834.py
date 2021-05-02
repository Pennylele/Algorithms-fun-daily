# think this problem is to find the relative point - 
# cur_nodes_sum = parent_node_sum - cur_nodes_children_sum (including the cur_node) + rest of the nodes.
# 0: 2 + 2 + 2 + 2; 2: 8 - 4 + 2
import collections
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        # build the graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # setup the 1D table
        children_nodes = [1] * N
        ans = [0] * N
        # count all the children nodes for each node
        def dfs(node = 0, parent = None):
            for v in graph[node]:
                if v != parent: # meaning this is not the leaf node
                    dfs(v, node)
                    children_nodes[node] += children_nodes[v]
                    ans[node] += ans[v] + children_nodes[v]

        # calculate all the sums for all the nodes
        def dfs2(node = 0, parent = None):
            for v in graph[node]:
                if v != parent:
                    ans[v] = ans[node] - children_nodes[v] + N - children_nodes[v]
                    dfs2(v, node)

        dfs()
        dfs2()
        return ans
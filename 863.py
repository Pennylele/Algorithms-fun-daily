class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # creating an undirected graph
        graph = collections.defaultdict(list)
        stack = [(root)]
        while stack:
            node = stack.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)
        
        # BFS
        stack = [target.val]
        seen = {target.val}
        for i in range(k):
            new_lst = []
            while stack:
                v = stack.pop()
                for nei in graph[v]:
                    if nei not in seen:
                        new_lst.append(nei)
                        seen.add(nei)
            stack = new_lst
        return stack
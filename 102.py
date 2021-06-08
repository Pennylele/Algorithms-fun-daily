# BFS METHOD
class Solution:
    def levelOrder(self, root):
        if not root: return []
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if len(res) < level + 1:
                res.append([])
            res[level].append(node.val)
            if node.right:
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))
        return res
#//////////////////////////DFS//////////////////////////////
class Solution:
    def levelOrder(self, root):
        def dfs(node, level):
            if not node: return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)
            return node


        res = []
        dfs(root, 0)
        return res
class Solution:
    def binaryTreePaths(self, root):
        ans = []
        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    ans.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)


        dfs(root, "")
        return ans
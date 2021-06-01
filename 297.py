#     1
#    / \
#   2   3
#      / \
#     4   5
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        ans = []

        def dfs(node): # preorder traversal
            if not node: ans.append("#")
            ans.append(root.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(ans) # "1,2,#,#,3,4,#,#,5,#,#"
    
    def deserialize(self, data):
        # data => "1,2,#,#,3,4,#,#,5,#,#"
        data = data.split(",")
        def dfs():
            if self.start == len(data):
                return
            if data[start] == "#":
                self.start += 1
                return None
            val = data[self.start]
            self.start += 1
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node

        self.start = 0
        return helper()
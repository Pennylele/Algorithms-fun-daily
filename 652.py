# we can write the serialized subtrees into a hashmap. 
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# defaultdict.default_factory = dictionary.__len__ => What seems to happen is that when we try to find a key that doesn’t exist in the dictionary, an entry gets created with a value equal to the number of items in the dictionary.
import collections
#/////////////////////////O(n^2)//////////////////////////////////////
class Solution:
    def findDuplicateSubtrees(self, root):
        def helper(node):
            if not node:
                return "#"
            struct = "{}, {}, {}".format(node.val, helper(node.left), helper(node.right)
            self.d[struct] += 1
            if self.d[struct] == 2:
                ans.append(node)
            return struct

        self.d = collections.defaultdict(int)
        ans = []
        helper(root)
        return ans
#/////////////////////////O(n)//////////////////////////////////////
class Solution:
    def findDuplicateSubtrees(self, root):
        # dfs function to pre-orderly traverse the tree to record all subtree patterns.
        def dfs(node):
            if node:
                uid = tree[(node.val, dfs(node.left), dfs(node.right))]
                counter[uid] += 1
                if counter[uid] == 2:
                    ans.append(node)
                return uid

        # A defaultdict to record uid/__len__ of the default_factory
        tree = collections.defaultdict()
        tree.default_factory = tree.__len__
        # A counter to record the frequencies of the uid
        counter = collections.Counter() # difference between Counter() and defaultdict(int)

        ans = []
        dfs(root)
        return ans

        
        
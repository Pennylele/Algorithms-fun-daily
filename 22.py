# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# The way I like to think about the runtime of backtracking algorithms is O(b^d), where b is the branching factor and d is the maximum depth of recursion.

# # Backtracking is characterized by a number of decisions b that can be made at each level of recursion. If you visualize the recursion tree, this is the number of children each internal node has. You can also think of b as standing for "base", which can help you remember that b is the base of the exponential.

# # If we can make b decisions at each level of recursion, and we expand the recursion tree to d levels (ie: each path has a length of d), then we get b^d nodes. Since backtracking is exhaustive and must visit each one of these nodes, the runtime is O(b^d).
# So at least we should come up with O(2^n)
class Solution:
    def generateParenthesis(self, n):
        ans = []

        def backtrack(left, right, path):
            if len(path) == n * 2:
                ans.append(path)
            if left < n:
                backtrack(left + 1, right, path + '(')
            if right < left:
                backtrack(left, right + 1, path + ')')

        backtrack(0, 0, '')
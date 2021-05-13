# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
class Solution:
    def longestIncreasingPath(self, matrix):
        R, C = len(matrix), len(matrix[0])
        self.memo = [[0] * C for _ in range(R)] # I think this also checks for whether a node is visited or not...

        def dfs(row, col):
            if not self.memo[row][col]:
                adj_cells = []
                for new_row, new_col in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                    if 0 <= new_row < R and 0 <= new_col < C and matrix[new_row][new_col] > matrix[row][col]:
                        adj_cells.append(dfs(new_row, new_col))
                self.memo[row][col] = max(adj_cells, default=0) + 1
            # print(self.memo)
            return self.memo[row][col]

        ans = 0
        for i in range(R):
            for j in range(C):
                ans = max(ans, dfs(i, j))
        return ans
# Call stack
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[1, 1, 0], [0, 0, 0], [0, 0, 0]]
# [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
# [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
# [[1, 1, 2], [0, 0, 1], [0, 0, 0]]
# [[1, 1, 2], [0, 0, 1], [0, 0, 0]]
# [[1, 1, 2], [2, 0, 1], [0, 0, 0]]
# [[1, 1, 2], [2, 0, 1], [0, 0, 0]]
# [[1, 1, 2], [2, 0, 1], [0, 0, 0]]
# [[1, 1, 2], [2, 2, 1], [0, 0, 0]]
# [[1, 1, 2], [2, 2, 1], [0, 0, 0]]
# [[1, 1, 2], [2, 2, 1], [0, 0, 0]]
# [[1, 1, 2], [2, 2, 1], [3, 0, 0]]
# [[1, 1, 2], [2, 2, 1], [3, 0, 0]]
# [[1, 1, 2], [2, 2, 1], [3, 0, 0]]
# [[1, 1, 2], [2, 2, 1], [3, 4, 0]]
# [[1, 1, 2], [2, 2, 1], [3, 4, 0]]
# [[1, 1, 2], [2, 2, 1], [3, 4, 2]]

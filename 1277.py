class Solution:
    def countSquares(self, matrix):
        if not len(matrix): return 0
        R, C = len(matrix), len(matrix[0])
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        
        # count the sum of the matrix
        ans = 0
        for i in range(R):
            for j in range(C):
                ans += matrix[i][j]
        return ans

s = Solution()
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
# edge case - matrix = [[]]
print(s.countSquares(matrix))
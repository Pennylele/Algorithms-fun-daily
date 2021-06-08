# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        # use prefix sum to calculate each row
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n-1):
                matrix[i][j+1] += matrix[i][j] # [[0,1,1],[1,2,3],[0,1,1]]

        # fixate the columns and calculate all the matrices
        res = 0
        for c1 in range(n): # fix the leftmost border - column1, column2, column3
            for c2 in range(c1, n): # expand the rightmost border
                presum = {0: 1}
                s = 0
                for x in range(m): # go down each row whjen the left and right borders are fixed.
                    s += matrix[x][c2] - (matrix[x][c1-1] if c1 > 0 else 0)
                    res += presum.get(s - target, 0)
                    presum[s] = presum.get(s, 0) + 1
        return res

obj = Solution()
print(obj.numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 3))

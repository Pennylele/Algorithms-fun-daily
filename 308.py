# Brute force would be to just sum the regions everytime we receive a request by O(n)
# But we can use fenwick tree to make the runtime faster. (2D tree)
class NumMatrix:
    def __init__(self, matrix):
        # build the tree
        self.R, self.C = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.BIT = [[0] * (self.C + 1) for _ in range(self.R + 1)] # skeleton to make a copy of the original matrix

        for i in range(1, self.R+1):
            for j in range(1, self.C+1):
                self.BIT[i][j] += self.matrix[i-1][j-1] # !!! IMPORTANT: use += here, not =. I think we should increment based on the existing value.
                ii = i + (i & -i)
                jj = j + (j & -j)
                if ii < self.R + 1 and jj < self.C + 1: # I think this is to remove the duplicated count
                    self.BIT[ii][jj] -= self.BIT[i][j]
                if ii < self.R + 1:
                    self.BIT[ii][j] += self.BIT[i][j]
                if jj < self.C + 1:
                    self.BIT[i][jj] += self.BIT[i][j]

    def update(self, row, col, val):
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        r, c = row + 1, col + 1

        while r < self.R + 1:
            next_c = c
            while next_c < self.C + 1:
                self.BIT[r][next_c] += diff
                next_c += next_c & -next_c
            r += (r & -r)

    def helper(self, row, col):
        result = 0
        r, c = row + 1, col + 1
        while r > 0:
            next_c = c
            while next_c > 0:
                result += self.BIT[r][next_c]
                next_c -= (next_c & - next_c)
            r -= (r & -r)
        return result


    def sumRegion(self, row1, col1, row2, col2):
        return self.helper(row2, col2) - self.helper(row2, col1 - 1) - self.helper(row1 - 1, col2) + self.helper(row1 - 1, col1 - 1)

# Driver Code
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3))




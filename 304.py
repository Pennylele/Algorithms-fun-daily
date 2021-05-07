# Can we use fenwick tree? - I'm thinking about using that.
# But if we don't.. I think we can precompute all the sums?

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Create another matrix where we store all the sums of regions with the left location being (0, 0)
        R, C = len(matrix), len(matrix[0])
        self.sum = [[0] * (C+1) for _ in range(R+1)]
        
        for i in range(1, R+1):
            for j in range(1, C+1):
                self.sum[i][j] = matrix[i-1][j-1] + self.sum[i][j-1] + self.sum[i-1][j] - self.sum[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Then we can perform the math to computer the desired region
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.sum[row2][col2] - self.sum[row2][col1-1] - self.sum[row1-1][col2] + self.sum[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
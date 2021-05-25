# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# transpose method + reverse the lists
class Solution:
    def rotate(self, matrix):
        R = len(matrix)
        for i in range(R): # O(R*R)
            for j in range(i, R):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for lst in matrix: #O(R*R)
            lst.reverse()
        return matrix
# Just update the cells in one pass
class Solution:
    def rotate(self, matrix):
        h = len(matrix)
        n = h - 1

        for row in range(h//2):
            for col in range(row, n-row):
                temp = matrix[row][col]
                matrix[row][col] = matrix[n-col][row]
                matrix[n-col][row] = matrix[n-row][n-col]
                matrix[n-row][n-col] = matrix[col][n-row]
                matrix[col][n-row] = temp
        return matrix
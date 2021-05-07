# Input: matrix = 
# [["1","0","1","0","0"],
#  ["1","0","1","1","1"],
#  ["1","1","1","1","1"],
#  ["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# create a dp array for each row => then use histogram to calculate the largest histogram area.
class Solution:
    def maximalRectangle(self, matrix):
        R, C = len(matrix), len(matrix[0])
        heights = [0] * (C+1) # we have one trailing [0] bc we can start compare the first element with heights[-1]
        res = 0
        for i in range(R):
            for j in range(C):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            
            # histogram for this row
            stack = [-1]
            for idx, height in enumerate(heights):
                while height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = idx - 1 - stack[-1]
                    area = h * w
                    res = max(res, area)
                stack.append(idx)
        return res

obj = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(obj.maximalRectangle(matrix))
                    


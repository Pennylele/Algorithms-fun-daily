# My own method
class Solution:
    def generate(self, numRows):
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(2, numRows):
            tmp = []
            for j in range(1, i):
                tmp.append(res[-1][j-1] + res[-1][j])
            res += [[1] + tmp + [1]]
        return res
# Official answer, kind of
class Solution:
    def generate(self, numRows):
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, row_num):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            
            triangle.append(row)
        return triangle

obj = Solution()
print(obj.generate(5))
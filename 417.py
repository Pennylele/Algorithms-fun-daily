# Input: heights = 
# [[1,2,2,3,5],
#  [3,2,3,4,4],
#  [2,4,5,3,1],
#  [6,7,1,4,5],
#  [5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# The target cell should be the largest among its own row and col. 
# And what's more important - the path needs to be in an descending order (from the highest point to the border)
class Solution:
    def pacificAtlantic(Self, heights):
        R, C = len(heights), len(heights[0])
        pacific = [[False] * C for _ in range(R)]
        atlantic = [[False] * C for _ in range(R)]

        def dfs(row, col, matrix):
            matrix[row][col] = True
            for new_row, new_col in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if 0 <= new_row < R and 0 <= new_col < C and not matrix[new_row][new_col] and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, matrix)


        for i in range(R):
            dfs(i, 0, pacific)
            dfs(i, C-1, atlantic)
        
        for j in range(C):
            dfs(0, j, pacific)
            dfs(R-1, j, atlantic)
        
        ans = []
        for i in range(R):
            for j in range(C):
                if pacific[i][j] == atlantic[i][j] == True:
                    ans.append([i, j])
        
        return ans
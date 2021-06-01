# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        def dfs(row, col):
            visited.add((row, col))
            image[row][col] = newColor
            for new_r, new_c in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if 0 <= new_r < R and 0 <= new_c < C and (new_r, new_c) not in visited and image[new_r][new_c] == oldColor:
                    dfs(new_r, new_c) 
        
        R, C = len(image), len(image[0])
        visited = set()
        dfs(sr, sc)
        return image
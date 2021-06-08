# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Time Complexity: O(N⋅3^L) where N is the number of cells in the board and L is the length of the word to be matched.
class Solution:
    def exist(self, board, word):
        def dfs(row, col, word):
            if len(word) == 0:
                return True
            if row < 0 or row >= R or col < 0 or col >= C or board[row][col] != word[0]:
                return False
            res = False
            # mark the choice before exploring further.
            board[row][col] = "#"
            for new_r, new_c in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                res = dfs(new_r, new_c, word[1:])
                if res: break # break instead of return directly to do some cleanup afterwards
                # Penny: My feeling is that this is like hitting a brake. Since this is the DFS, so we traversal all the way to the leave (if possible), the "break" wouldn't work until we are returning to the previous stacks. In Example 3, we go all the way to [['#', '#', '#', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], and then when coming back, we hit break every time we see a "#", cause res was True. So we return the them back to its original character which is stored in word[0]
            board[row][col] = word[0]
            return res

        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                if dfs(i, j, word):
                    return True
        return False
#///////////////////////////////////////////////////////////////////////
# Or just like this
class Solution:
    def exist(self, board, word):    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word):
                    return True
        return False
    
    def helper(self, board, i, j, word):
        if len(word) == 0:
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        
        
        tmp = board[i][j]
        board[i][j] = "#"
        
        found = self.helper(board, i+1, j, word[1:]) or self.helper(board, i-1, j, word[1:]) or self.helper(board, i, j+1, word[1:]) or self.helper(board, i, j-1, word[1:])
        
        board[i][j] = tmp
        
        return found

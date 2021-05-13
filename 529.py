class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        
        def dfs(r, c):
            if board[r][c] != 'E':
                return
            bomb_count = 0
            for new_r, new_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c-1), (r+1, c-1), (r-1, c+1):
                if 0 <= new_r < R and 0 <= new_c < C and board[new_r][new_c] == 'M':
                    bomb_count += 1
            if bomb_count == 0:
                board[r][c] = 'B'
            else:
                board[r][c] = str(bomb_count)
                return # this return is important, bc we want to stop traverse from here
            for new_r, new_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c-1), (r+1, c-1), (r-1, c+1):
                if 0 <= new_r < R and 0 <= new_c < C:
                    dfs(new_r, new_c)
        
        
        row, col = click[0], click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        else:
            dfs(row, col)
            
        return board
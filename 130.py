# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
class Solution:
    def solve(self, board):
        R, C = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            board[r][c] = "#"
            for new_r, new_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= new_r < R and 0 <= new_c < C and (new_r, new_c) not in visited and board[new_r][new_c] == "O":
                    visited.add((new_r, new_c))
                    dfs(new_r, new_c)

        for i in range(R):
            for j in range(C):
                if (i == 0 or j == 0 or i == R - 1 or j == C - 1) and board[i][j] == "O": 
                    dfs(i, j)
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
        return board

obj = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(obj.solve(board))


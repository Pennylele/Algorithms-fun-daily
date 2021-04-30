import collections
# target = "leet"
class Solution:
    def alphabetBoardPath(self, target):
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        # Main BFS function
        def bfs(row, col, dest):
            if board[row][col] == dest:
                return row, col, "!"
            visited = {(row, col)}
            q = collections.deque([(row, col, '')])
            while q:
                r, c, p = q.popleft()
                for new_r, new_c, new_p in (r+1, c, 'D'), (r, c+1, 'R'), (r-1, c, 'U'), (r, c-1, 'L'):
                    if 0 <= new_r < 6 and 0 <= new_c < len(board[new_r]) and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        if board[new_r][new_c] == dest:
                            return new_r, new_c, p + new_p + "!"
                        else:
                            q.append((new_r, new_c, new_p + p))


    # main function to start BFS everytime we find the next destination
        ans = ""
        i, j = 0, 0
        for dest in target:
            i, j, path = bfs(i, j, dest)
            ans += path
        return ans

# Unit Tests
def test_func():
    obj = Solution()
    result = obj.alphabetBoardPath("leet")
    assert result == "DDR!URRRU!!DDD!", "DDR!UURRR!!DDD!"
    print("success!")

test_func()
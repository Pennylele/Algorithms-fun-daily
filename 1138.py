# ////////////////////////BFS kinda slow//////////////////////////////
# target = "leet"
class Solution:
    def alphabetBoardPath(self, target):
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        def bfs(r, c, target):
            if board[r][c] == target:
                return r, c, "!"
            q = collections.deque([(r, c, "")])
            visited = {(r, c)}
            while q:
                row, col, path = q.popleft()
                for new_r, new_c, new_p in (row+1, col, "D"), (row-1, col, "U"), (row, col+1, "R"), (row, col-1, "L"):
                    if 0 <= new_r < R and 0 <= new_c < len(board[new_r]) and board[new_r][new_c] not in visited:
                        visited.add((new_r, new_c, new_p))
                        if board[new_r][new_c] == target:
                            return new_r, new_c, path + new_p + "!"
                        else:
                            q.append((new_r, new_c, path + new_p))

        ans = []
        i, j = 0, 0
        R, C = len(board), len(board[0])
        for ch in target:
            i, j, path = bfs(row, col, ch)
            ans += path
        return "".join(ans)
# ////////////////////////Another faster solution//////////////////////////////
# Remember to travel left and up before down and right. Edge case: "zdz"
class Solution:
    def alphabetBoardPath(self, target):
        start_x, start_y = 0, 0
        ans = []
        for ch in target:
            num = ord(ch) - 97
            target_x, target_y = num // 5, num % 5
            if target_y < start_y:
                path = (start_y - target_y) * "L"
                ans.append(path)
            if start_x < target_x:
                path = (target_x - start_x) * "D"
                ans.append(path)
            if start_x > target_x:
                path = (start_x - target_x) * "U"
                ans.append(path)
            if target_y > start_y:
                path = (target_y - start_y) * "R"
                ans.append(path)
            ans.append("!")
            start_x, start_y = target_x, target_y
        
        return "".join(ans)

# Unit Tests
def test_func():
    obj = Solution()
    result = obj.alphabetBoardPath("leet")
    assert result == "DDR!URRRU!!DDD!", "DDR!UURRR!!DDD!"
    print("success!")

test_func()
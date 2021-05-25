# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# directions (0, 1), (1, 0), (0, -1), (-1, 0)
class Solution:
    def spiralOrder(self, matrix):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in range(R)]
        r, c, di = 0, 0, 0
        ans = []

        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True

            new_r = r + directions[di][0]
            new_c = c + directions[di][1]

            if 0 <= new_r < R and 0 <= new_c < C and not seen[new_r][new_c]:
                r, c = new_r, new_c
            else:
                di = (di + 1) % 4
                r, c = r + directions[di][0], c + directions[di][1]
        return ans
# /////////////////Or use extend, saving space////////////////////
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
# Output: [1,2,3,6,9,8,7,4,5]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m-1, 0, n-1
        
        while l < r and u < d:
            res.extend([matrix[u][i] for i in range(l, r)])
            res.extend([matrix[j][r] for j in range(u, d)])
            res.extend([matrix[d][i] for i in range(r, l, -1)])
            res.extend([matrix[j][l] for j in range(d, u, -1)])
            u, d, l, r = u+1, d-1, l+1, r-1
            print(u,d,l,r)
        
        if u == d: # I think we only consider when the last arrow is to the right or down. Because the above code (4 extends) go a full cycle every time.
            res.extend([matrix[u][i] for i in range(l, r+1)])
        elif l == r:
            res.extend([matrix[j][l] for j in range(u, d+1)])
        return res

obj = Solution()
print(obj.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
         



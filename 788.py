# /////////////////////O(nlogn)//////////////////////////
# class Solution:
#     def rotatedDigits(self, n: int) -> int:
#         valid = {'0', '1', '8', '2', '5', '6', '9'}
#         unchanged = {'0', '1', '8'}
#         def validate(num):
#             s = set([i for i in str(num)])
#             return s.issubset(valid) and not s.issubset(unchanged)
            
#         ans = 0
#         for i in range(n+1):
#             if validate(i) != False:
#                 ans += 1
#         return ans
#/////////////////////////O(logn)//////////////////////////////
class Solution:
    def rotatedDigits(self, n):
        valid = {0, 1, 8, 2, 5, 6, 9}
        unchanged = {0, 1, 8}
        A = list(map(int, str(n)))
        print(A)
        n = len(A)
        ans = 0
        has2569 = 0

        for i in range(n): # "25" => [2, 4] => 19, 23(X)
            for j in range(A[i]):
                print(j)
                if j in valid:
                    ans += 7 ** (n-1-i)
                if not has2569 and j in unchanged:
                    ans -= 3 ** (n-i-1)
                print("ans = " + str(ans))
            if A[i] not in valid:
                return ans
            elif A[i] in (valid - unchanged):
                has2569 = 1
                print(A[i], has2569)
        return ans + has2569

obj = Solution()
print(obj.rotatedDigits(24))


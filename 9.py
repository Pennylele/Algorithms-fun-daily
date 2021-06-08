# Input: x = 121
# Output: true
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# 121 % 10 = 1 => 0 * 10 + 1
# 12 % 10 = 2 => 1 * 10 + 2
# 1 % 10 = 1 => 12 * 10 + 1
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = 0
        origin = x
        while x > 0:
            num = num * 10 + x % 10 
            x //= 10
        return num == origin

obj = Solution()
print(obj.isPalindrome(121))

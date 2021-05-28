# Reverse a number is a good building block
class Solution:
    def reverse(self, x):
        result = 0

        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        # classic template for piecing the digits together in a 10-based system
        while x:
            result += result * 10 + x % 10
            x //= 10
        
        return 0 if result > pow(2, 31) else result * symbol
        

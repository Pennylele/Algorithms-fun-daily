# 2 ** 10
class Solution:
    def myPow(self, x, n):
        isNeg = False
        if n < 0:
            isNeg = True
            n = -n
        
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            h = n // 2
            half = helper(x, h)

            if n % 2 == 0:
                return half * half
            elif n % 2 == 1:
                return half * half * x 
        
        result = helper(x, n)
        return result if not isNeg else 1/result


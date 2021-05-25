# Input: x = 4
# Output: 2

# Input: x = 8
# Output: 2

class Solution:
    def mySqrt(self, x):
        if x < 2: return x
        l, r = 2, x // 2
        
        while l <= r:
            mid = l + (r-l)//2
            pivot = mid * mid
            
            if pivot < x:
                l = mid + 1
            elif pivot > x:
                r = mid - 1
            else:
                return mid
        return r
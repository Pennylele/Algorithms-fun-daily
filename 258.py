# ///////////////////The solution with loops///////////////////
class Solution:
    def addDigits(self, num: int) -> int:
        digital_root = 0
        while num:
            digital_root += num % 10
            num //= 10
            
            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0
        
        return digital_root
# ///////////////////The solution without loops/////////////////
class Solution:
    def addDigits(self, num):
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
# "199100199" => try out different combinations; process 3 numbers at a time; check whether the first 2 numbers' sum is the prefix of the 3rd number.
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        # summation function
        def add(num1, num2):
            a, b = len(num1)-1, len(num2)-1
            carryover = 0
            result = []
            while a >= 0 and b >= 0:
                carryover, digit = divmod(int(num1[a]) + int(num2[b]) + carryover, 10)
                result.append(str(digit)) # don't forget to append the string type
                a -= 1
                b -= 1
            
            while a >= 0:
                carryover, digit = divmod(int(num1[a]) + carryover, 10)
                result.append(str(digit))
                a -= 1
                
            while b >= 0:
                carryover, digit = divmod(int(num2[b]) + carryover, 10)
                result.append(str(digit))
                b -= 1
            
            if carryover: 
                result.append('1')
            
            return "".join(result[::-1])
        
        # DFS to check whether we can validate this is a additive number
        def dfs(num1, num2, num3):
            # edge case check
            if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0') or (len(num3) > 1 and num3[0] == '0'): # Need to place len(num1) > 1 for exmaple, otherwise we may get a index out of rnage error
                return False
            
            SUM = add(num1, num2)
            
            # stopping point of one dfs round
            if SUM == num3: 
                return True
            
            x = len(SUM)
            if len(num3) < x:
                return False
            
            if num3[:x] == SUM:
                return dfs(num2, SUM, num3[x:])
            else:
                return False
        
                                    
        # Driver's Code
        N = len(num)
        for i in range(N):
            for j in range(i):
                num1 = num[:j+1]
                num2 = num[j+1:i+1]
                num3 = num[i+1:]
                
                if dfs(num1, num2, num3):
                    return True
        return False
        
        
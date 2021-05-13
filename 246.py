class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        convert = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        N = len(num)
        res = []
        for i in range(N-1, -1, -1):
            if num[i] not in convert:
                return False
            res.append(convert[num[i]])
        
        return "".join(res) == num
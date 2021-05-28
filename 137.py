# 3 Duplicates and one unique value. 
# NEED TO FIND SOMEONE TO FIGURE THIS ONE OUT
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t1, t2 = 0, 0
        for num in nums:
            t1 = (~t2) & (t1 ^ num)
            t2 = (~t1) & (t2 ^ num)
        return t1
# We can keep track of the first, second nums, and then when we find the 3rd largest, we can return True
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float('inf')
        second_num = float('inf')
        
        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True
        return False
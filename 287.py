# Input: nums = [1,3,4,2,2]
# Output: 2
# can use slow and fast pointer for to satisfy this problem's requirements - not modifying the existing input list and O(1) time complexity
class Solution:
    def findDuplicate(self, nums):
        slow = fast = finder = 0

        # let the slow and faster pointer meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                # use finder to find the repeated element
                while nums[finder] != nums[slow]:
                    finder = nums[finder]
                    slow = nums[slow]
                    if finder == slow:
                        return finder




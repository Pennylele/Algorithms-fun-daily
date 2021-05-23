class Solution:
    def numComponents(self, head, nums):
        set_nums = set(nums)
        ans = 0
        
        while head:
            if head.val in set_nums and (head.next == None or head.next.val not in set_nums):
                ans += 1
            head = head.next
        return ans
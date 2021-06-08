# use slow and fast pointer to find the middle point.
class Solution:
    def isPalindrome(self, head):
        slow = fast = head
        # slow and fast pointer to find the mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the linked list
        prev = None
        while slow:
            nxt = slow.next # we need the nxt to record the slow.next since it's gonna change in the next line
            slow.next = prev
            prev = slow
            slow = nxt
        
        # check if palindrome
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        adder = 0
        while l1 or l2 or adder:
            if l1:
                adder += l1.val
                l1 = l1.next
            if l2:
                adder += l2.val
                l2 = l2.next
            cur.next = ListNode(adder % 10)
            adder //= 10
            cur = cur.next
        return dummy.next

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        start = dummy # starting traversing from one node ahead of head since we are checking the cur.next
        
        while start != None and start.next != None:
            if start.next.val == val:
                start.next = start.next.next
            else:
                start = start.next
        return dummy.next

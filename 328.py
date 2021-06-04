# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)

        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next # this makes sure that the even.next would be the first one to reach a None
            head = head.next.next if even.next # check in here if we continue moving on
        odd.next = dummy2.next
        return dummy1.next

class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next: # pay attention to the limit for the while loop
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
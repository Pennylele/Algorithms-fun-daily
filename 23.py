# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
class Solution:
    def mergeKLists(self, lists):
        if not lists: return None
        if len(lists) == 1: return lists[0]
        L = len(lists)
        mid = L // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l1, l2):
        dummy = p = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return dummy.next

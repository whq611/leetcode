class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self,l1,l2):
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next,l1 = l1,l1.next
            else:
                cur.next,l2 = l2,l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dum.next

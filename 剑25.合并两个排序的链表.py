class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = tmp = ListNode(-1)
        a,b = l1,l2
        while a and b:
            if a.val>b.val:
                tmp.next = ListNode(b.val)
                tmp = tmp.next
                b = b.next
            else:
                tmp.next = ListNode(a.val)
                tmp = tmp.next
                a = a.next
        while a:
            tmp.next = ListNode(a.val)
            tmp = tmp.next
            a = a.next
        while b:
            tmp.next = ListNode(b.val)
            tmp = tmp.next
            b = b.next
        return res.next

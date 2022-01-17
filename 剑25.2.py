class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        pre = None
        if l1.val < l2.val:
            pre = l1
            pre.next = self.mergeTwoList(l1.next,l2)
        else:
            pre = l2
            pre.next = self.mergeTwoList(l1,l2.next)
        return pre

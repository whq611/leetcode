class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a,b = headA,headB
        while a != b:
            if a.next and b.next:
                a = a.next
                b = b.next
            elif b.next and not a.next:
                a = headB
                b = b.next
            elif a.next and not b.next:
                b = headA
                a = a.next
            else:
                return None
        return a

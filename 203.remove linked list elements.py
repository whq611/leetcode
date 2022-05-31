def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prehead = ListNode(-1,head)
        pre = prehead
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next                
            else:
                pre = cur
            cur = cur.next
            
        return prehead.next

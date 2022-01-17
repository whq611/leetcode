class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self,head,val):
        if head.val == val:
            return head.next
        res = head
        i,j = head,head.next
        while j.val != val:
            i,j = i.next,j.next
        i.next = j.next
        return res

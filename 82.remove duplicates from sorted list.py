# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        a = pre = ListNode(-101,head)
        while cur:
            if cur.next==None or cur.next.val!=cur.val:
                pre.next = cur
                pre = cur
            while cur.next and cur.next.val==cur.val:
                cur.next = cur.next.next
            cur = cur.next
        pre.next = None
        return a.next

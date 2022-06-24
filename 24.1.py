# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        prehead = ListNode(-1,head)
        pre = prehead
        cur = head
        while cur and cur.next:
            pre.next = cur.next
            tmp = cur.next.next
            cur.next.next = cur
            cur.next = tmp
            pre = pre.next.next
            cur = cur.next
        return prehead.next

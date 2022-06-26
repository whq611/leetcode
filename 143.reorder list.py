# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        a,b = head,pre
        while b.next:
            tmp1 = a.next
            tmp2 = b.next
            a.next = b
            b.next = tmp1
            b = tmp2
            a = tmp1

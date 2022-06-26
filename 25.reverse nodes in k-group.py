# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prehead = ListNode(-1,head)
        pre = prehead
        cur = head
        l = 0
        while head:
            l+=1
            head = head.next
        for i in range(l//k):
            for j in range(k-1):
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            pre = cur
            cur = pre.next
        return prehead.next

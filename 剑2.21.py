# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prehead = ListNode(-1,head)
        slow = fast = prehead
        while n>0:
            fast = fast.next
            n-=1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return prehead.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            pre = None
            while head:
                tmp = head.next
                head.next = pre
                pre = head
                head = tmp
            return pre
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        head = None
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            val = (carry+x+y)%10
            carry = (carry+x+y)//10
            curr = ListNode(val)
            curr.next = head
            head = curr
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return head

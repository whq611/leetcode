# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        a = slow.next

        while a:
            tmp = a.next
            a.next = slow
            slow = a
            a = tmp
            
           
        while head.next!=slow and head.next!=slow.next:
            if head.val!=slow.val: return False
            head = head.next
            slow = slow.next
        if head.val!=slow.val: return False 
        return True

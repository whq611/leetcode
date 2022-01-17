class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def getKthFromEnd(self,head,k):
        a = b = head
        for _ in range(k):
            b = b.next
        while b:
            a = a.next
            b = b.next
        return a

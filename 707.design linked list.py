class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.preHead = ListNode(-1)


    def get(self, index: int) -> int:
        cur = self.preHead
        while cur.next and index>=0:
            cur = cur.next
            if index==0:
                return cur.val
            index-=1
            
        return -1
        


    def addAtHead(self, val: int) -> None:
        cur = ListNode(val,self.preHead.next)
        self.preHead.next = cur

    def addAtTail(self, val: int) -> None:
        cur = self.preHead
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)


    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.preHead
        while cur and index>=0:
            
            if index==0:
                a = ListNode(val,cur.next)
                cur.next = a
            cur = cur.next
            index-=1
            


    def deleteAtIndex(self, index: int) -> None:
        cur = self.preHead
        while cur and index>=0:
            
            if index==0 and cur.next: cur.next = cur.next.next
            cur = cur.next
            index-=1

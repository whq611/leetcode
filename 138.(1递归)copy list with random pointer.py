class Node:
    def __init__(self,x=None,next=None,random=None):
        self.x = int(x)
        self.next = next
        self.random = random
class Solution:
    def __init__(self):
        self.visitedHash = {}
    def copyRandomList(self,head):
        if head == None:
            return None
        if head in self.visitedHash:
            return self.visitedHash[head]
        node = Node(head.val,None,None)
        self.visitedHash[head] = node
        node.next = self.self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
